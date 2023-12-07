from pathlib import Path

import pygame

from level.tank import Tank


class Player(Tank):
    def __init__(self, game, start_pos, start_angle, bullets_group, walls):
        super(Player, self).__init__(game, f"{game.sprite_dir}/player_tank.png", start_pos, start_angle, bullets_group, walls)
        self.health = 1

    def update(self, delta_time, actions):
        if actions['left']:
            self.rotate(self.ROTATION_SPEED)
        elif actions['right']:
            self.rotate(-self.ROTATION_SPEED)

        if actions['up']:
            self.move(self.direction, self.walls)
        elif actions['down']:
            self.move(-self.direction, self.walls)

        if actions['space'] and ((delta_time - self.last_shot_time >= self.shoot_cooldown) or self.last_shot_time == 0):
            self.shoot()
            self.last_shot_time = delta_time
