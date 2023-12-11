import pygame

from level.enemy import Enemy
from level.player import Player
from level.map import Map
from states.game_over import GameOver
from states.pause_menu import PauseMenu
from states.state import State

from level.audio import *


class Level(State):
    def __init__(self, game, number, status='locked'):
        State.__init__(self, game)
        self.number = number
        self.status = status
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.map = Map(self.game, number)
        self.player = Player(self.game, (5 * self.game.TILE_SIZE, 4 * self.game.TILE_SIZE), 225, self.bullets,
                             self.map.wall_positions)

        self.level_init()

    def update(self, delta_time, actions):
        if len(self.enemies) < 1:
            if self.number < len(self.game.levels):
                self.game.levels[(self.number + 1)].status = 'unlocked'
            self.level_init()
            next_state = GameOver(self.game, True)
            next_state.enter_state()
        if self.player.health <= 0:
            tank_explosion_sound()
            self.level_init()
            next_state = GameOver(self.game, False)
            next_state.enter_state()

        if actions["escape"]:
            next_state = PauseMenu(self.game, self)
            next_state.enter_state()

        self.player.update(delta_time, actions)
        self.enemies.update(delta_time)
        self.bullets.update(self.player, self.enemies)

    def render(self, display):
        display.blit(self.map.background, (0, 0))
        self.player.render(display)
        self.enemies.draw(display)
        self.bullets.draw(display)
        for enemy in self.enemies:
            enemy.draw_path(display)
            pygame.draw.rect(display, (0, 0, 255), enemy.pathfinding_hitbox, 2)  # Draw the enemy rect
            pygame.draw.circle(display, (0, 0, 255), enemy.rect.center, 2)  # Draw the enemy center
            enemy.draw_line_of_sight(display)
            enemy.draw_hitbox(display)
            pygame.draw.rect(display, (255, 255, 0), enemy.wall_hitbox, 2)
            if enemy.next_waypoint_rect:
                pygame.draw.rect(display, (0, 255, 0), enemy.next_waypoint_rect, 2)

    def level_init(self):
        self.enemies.empty()
        self.bullets.empty()
        self.map.wall_positions.clear()

        self.map.load_textures()
        self.map.initialize_map_tiles()

        if self.number == 1:
            self.player = Player(self.game, (5 * self.game.TILE_SIZE, 4 * self.game.TILE_SIZE), 225, self.bullets,
                                 self.map.wall_positions)

            self.spawn_enemy((self.game.WIDTH - 5 * self.game.TILE_SIZE, self.game.HEIGHT - 4 * self.game.TILE_SIZE),
                             45)
        elif self.number == 2:
            self.player = Player(self.game, (5 * self.game.TILE_SIZE, 4 * self.game.TILE_SIZE), 225, self.bullets,
                                 self.map.wall_positions)

            self.spawn_enemy((self.game.WIDTH - 5 * self.game.TILE_SIZE, self.game.HEIGHT - 4 * self.game.TILE_SIZE),
                             45)
            self.spawn_enemy((self.game.WIDTH - 5 * self.game.TILE_SIZE, 4 * self.game.TILE_SIZE), 135)
        elif self.number == 3:
            self.player = Player(self.game, (5 * self.game.TILE_SIZE, 4 * self.game.TILE_SIZE), 225, self.bullets,
                                 self.map.wall_positions)

            self.spawn_enemy((self.game.WIDTH - 5 * self.game.TILE_SIZE, self.game.HEIGHT - 4 * self.game.TILE_SIZE),
                             45)
        
        



    def spawn_enemy(self, pos, start_angle):
        enemy = Enemy(self.game, pos, start_angle, self.player, self.bullets, self.map.wall_positions)
        self.enemies.add(enemy)
