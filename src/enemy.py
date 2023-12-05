import math

import pygame

from tank import Tank


class Enemy(Tank):
    def __init__(self, screen, start_pos, player, bullets_group, walls):
        super(Enemy, self).__init__(screen, 'assets/tanks/enemy_tank.png', start_pos, 90, bullets_group, walls)
        self.player = player
        self.FORWARD_VELOCITY = 3
        self.ROTATION_SPEED = 2
        self.shooting_range = 300
        self.shooting_angle = 4

        self.shoot_cooldown = 2000
        self.last_shot_time = 0

        self.action_cooldown = 500
        self.last_action_time = 0

        self.state = "idle"

    def update(self, current_time):
        self.determine_action(current_time)

    def determine_action(self, current_time):
        distance = self.calculate_distance_to_player()
        angle_difference = self.calculate_angle_difference_to_player()

        if self.state == "rotating":
            if angle_difference*5 >= self.shooting_angle:
                self.rotate_towards_player()
            else:
                self.state = "idle"

        elif self.state == "moving":
            if angle_difference >= self.shooting_angle:
                self.state = "idle"
            elif distance > self.shooting_range:
                self.move_towards_player()
            else:
                self.state = "idle"

        elif self.state == "shooting":
            if self.can_shoot():
                self.shoot()
            else:
                self.state = "idle"
        elif self.state == "idle" and current_time - self.last_action_time >= self.action_cooldown:
            if angle_difference >= self.shooting_angle:
                self.state = "rotating"
                self.last_action_time = current_time
            elif distance > self.shooting_range:
                self.state = "moving"
                self.last_action_time = current_time
            elif current_time - self.last_shot_time >= self.shoot_cooldown:
                self.state = "shooting"
                self.last_action_time = current_time


    def calculate_distance_to_player(self):
        return math.hypot(self.player.rect.centerx - self.rect.centerx, self.player.rect.centery - self.rect.centery)

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
        distance = self.calculate_distance_to_player()
        angle_difference = self.calculate_angle_difference_to_player()

        # Check if player is within shooting range and angle
        if distance <= self.shooting_range and angle_difference <= self.shooting_angle:
            if pygame.time.get_ticks() - self.last_shot_time >= self.shoot_cooldown:
                return True
        return False

    def shoot(self):
        super(Enemy, self).shoot()
        self.last_shot_time = pygame.time.get_ticks()
