import pygame

from tank import Tank


class Player(Tank):
    def __init__(self, screen, start_pos, start_angle, bullets_group, walls):
        super(Player, self).__init__(screen, 'assets/tanks/player_tank.png', start_pos, start_angle, bullets_group, walls)
        self.health = 1

    def update(self, pressed_keys, current_time):
        if pressed_keys[pygame.K_LEFT]:
            self.rotate(self.ROTATION_SPEED)
        elif pressed_keys[pygame.K_RIGHT]:
            self.rotate(-self.ROTATION_SPEED)

        if pressed_keys[pygame.K_UP]:
            self.move(self.direction, self.walls)
        elif pressed_keys[pygame.K_DOWN]:
            self.move(-self.direction, self.walls)

        if pressed_keys[pygame.K_SPACE] and ((current_time - self.last_shot_time >= self.shoot_cooldown) or self.last_shot_time == 0):
            self.shoot()
            self.last_shot_time = current_time
