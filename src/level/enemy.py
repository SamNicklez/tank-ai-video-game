import math

import pygame

from level.pathfinding import line_intersects_rect, find_path, simplify_zigzags
from level.tank import Tank


class Enemy(Tank):
    def __init__(self, game, start_pos, start_angle, player, bullets_group, walls):
        Tank.__init__(self, game, f"{game.sprite_dir}/enemy_tank.png", start_pos, start_angle, bullets_group,
                      walls)

        self.player = player
        self.FORWARD_VELOCITY = 5
        self.ROTATION_SPEED = 3
        self.shooting_angle = 2

        self.shoot_cooldown = 2000
        self.last_shot_time = 0

        self.action_cooldown = 500
        self.last_action_time = 0

        self.pathfinding_cooldown = 200
        self.last_pathfinding_time = 0

        self.state = "idle"
        self.path = []
        self.path_index = 0

        self.next_pos = None
        self.next_waypoint_rect = None

    def update(self, current_time):
        if current_time - self.last_action_time >= self.action_cooldown:
            self.determine_action(current_time)
            self.last_action_time = current_time
        # Existing movement logic
        if self.state == "rotating":
            self.rotate_towards_player()
        elif self.state == "pathing":
            self.move_along_path()
        elif self.state == "shooting":
            if self.can_shoot():
                self.shoot()

    def determine_action(self, current_time):
        if self.has_line_of_sight():
            self.orient_and_attack()
        else:
            self.pathfind_to_player(current_time)

    def orient_and_attack(self):
        angle_difference = self.calculate_angle_difference_to_player()

        if angle_difference >= self.shooting_angle:
            self.state = "rotating"
        else:
            self.state = "shooting"

    def pathfind_to_player(self, current_time):
        if current_time - self.last_pathfinding_time >= self.pathfinding_cooldown or self.last_pathfinding_time == 0:
            raw_path = find_path(self.rect.center, self.player.rect.center, self.walls)
            self.path = simplify_zigzags(raw_path, self.walls)
            self.last_pathfinding_time = current_time
        self.path_index = 1
        self.state = "pathing"



    def move_along_path(self):
        if self.path_index < len(self.path):
            # Move to the next waypoint in the path
            self.move_to(self.path[self.path_index])

            # Create a rect for the next waypoint
            waypoint_rect = pygame.Rect(
                self.path[self.path_index][0] - self.game.TILE_SIZE // 2,
                self.path[self.path_index][1] - self.game.TILE_SIZE // 2,
                self.game.TILE_SIZE,
                self.game.TILE_SIZE
            )

            # Check if the enemy's hitbox collides with the rect of the next waypoint
            if self.rect.center == waypoint_rect.center:
                # Move to the next waypoint
                self.path_index += 1

            if self.path_index >= len(self.path):
                self.path = []
                self.state = "idle"

            # If the path index reaches the end, clear the path
            if self.path_index >= len(self.path):
                self.path = []
                self.state = "idle"

            self.next_waypoint_rect = waypoint_rect

    def move_to(self, pos):
        # Calculate direction from the enemy to the target waypoint
        direction_vector = pygame.math.Vector2(pos[0] - self.rect.centerx, pos[1] - self.rect.centery)
        distance_to_waypoint = direction_vector.length()
        if distance_to_waypoint > 0:
            direction_vector.normalize_ip()

        # Rotate towards the target waypoint

        target_angle = direction_vector.angle_to(pygame.math.Vector2(0, -1))
        target_angle = round(target_angle)
        angle_difference = (target_angle - self.angle + 360) % 360
        if angle_difference > 180:
            angle_difference -= 360

        # If angle difference is significant, rotate first
        if abs(angle_difference) > self.ROTATION_SPEED:
            self.rotate(math.copysign(self.ROTATION_SPEED, angle_difference))
        elif abs(angle_difference) > 0:
            self.rotate(angle_difference)
        else:
            if distance_to_waypoint > self.FORWARD_VELOCITY:
                self.move(direction_vector, self.walls)
            elif distance_to_waypoint > 0:
                self.rect.move_ip(self.direction * distance_to_waypoint)

            self.pathfinding_hitbox.center = self.rect.center
            self.wall_hitbox.center = self.rect.center

    def move(self, direction, walls):
        new_position = self.wall_hitbox.copy()
        new_position.move_ip(direction * self.FORWARD_VELOCITY)
        if not self.check_collisions(new_position, walls):
            self.rect.center = new_position.center
            self.pathfinding_hitbox.center = self.rect.center
            self.wall_hitbox.center = self.rect.center

    def calculate_angle_difference_to_player(self):
        dx = self.player.rect.centerx - self.rect.centerx
        dy = self.player.rect.centery - self.rect.centery

        # Angle from the enemy to the player in standard mathematical coordinates
        math_angle_to_player = math.degrees(math.atan2(-dy, dx))

        # Transform to Pygame's coordinate system (0 degrees is up, and angles increase clockwise)
        angle_to_player = (math_angle_to_player - 90) % 360

        enemy_angle = self.angle % 360

        # Calculate the minimum angle difference
        angle_difference = (angle_to_player - enemy_angle + 360) % 360
        angle_difference = min(angle_difference, 360 - angle_difference)
        return angle_difference

    def rotate_towards_player(self):
        dx, dy = self.player.rect.centerx - self.rect.centerx, self.player.rect.centery - self.rect.centery
        angle_to_player = math.degrees(math.atan2(-dy, dx)) - 90

        angle_difference = (angle_to_player - self.angle + 180 + 360) % 360 - 180
        if abs(angle_difference) > self.ROTATION_SPEED:
            self.rotate(math.copysign(self.ROTATION_SPEED, angle_difference))
        else:
            self.rotate(angle_difference)  # Make the final adjustment

    def move_towards_player(self):
        # Move towards the player
        self.move(self.direction, self.walls)

    def can_shoot(self):
        angle_difference = self.calculate_angle_difference_to_player()

        # Check if player is within shooting range and angle
        if angle_difference <= self.shooting_angle:
            if pygame.time.get_ticks() - self.last_shot_time >= self.shoot_cooldown:
                return True
        return False

    def shoot(self):
        super(Enemy, self).shoot()
        self.last_shot_time = pygame.time.get_ticks()

    def has_line_of_sight(self):
        start = pygame.math.Vector2(self.rect.center)
        end = pygame.math.Vector2(self.player.rect.center)

        for wall in self.walls:
            if line_intersects_rect(start, end, wall):
                return False
        return True

    def draw_path(self, surface):
        if self.path and len(self.path) > 1:
            # Set the color and width of the path line
            path_color = (255, 0, 0)  # Red color
            path_width = 2  # 2 pixels thick

            # Draw lines between each point in the path
            pygame.draw.lines(surface, path_color, False, self.path, path_width)

    def draw_line_of_sight(self, surface):
        start = pygame.math.Vector2(self.rect.center)
        end = pygame.math.Vector2(self.player.rect.center)

        for wall in self.walls:
            if line_intersects_rect(start, end, wall):
                return

        pygame.draw.lines(surface, (255, 0, 0), False, [start, end], 4)

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)
