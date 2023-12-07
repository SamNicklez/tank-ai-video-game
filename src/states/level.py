import pygame

from level.enemy import Enemy
from level.player import Player
from map import Map
from states.game_over import GameOver
from states.state import State


# from states.pause_menu import PauseMenu


class Level(State):
    def __init__(self, game, number, status='locked'):
        State.__init__(self, game)
        self.number = number
        self.status = status
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.map = Map(self.game.WIDTH, self.game.HEIGHT, self.game.TILE_SIZE)
        self.player = Player(self.game, (4 * self.game.TILE_SIZE, 3 * self.game.TILE_SIZE), 225, self.bullets,
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
            self.level_init()
            next_state = GameOver(self.game, False)
            next_state.enter_state()

        if actions["escape"]:
            pass

        self.player.update(delta_time, actions)
        self.enemies.update(delta_time)
        self.bullets.update(self.player, self.enemies)

    def render(self, display):
        display.blit(self.map.background, (0, 0))
        self.player.render(display)
        self.enemies.draw(display)
        self.bullets.draw(display)

    def level_init(self):
        self.enemies.empty()
        self.bullets.empty()
        self.map.wall_positions.clear()

        self.map.load_textures()
        self.map.initialize_map_tiles()

        self.player = Player(self.game, (4 * self.game.TILE_SIZE, 3 * self.game.TILE_SIZE), 225, self.bullets,
                             self.map.wall_positions)

        self.spawn_enemy((self.game.WIDTH - 4 * self.game.TILE_SIZE, self.game.HEIGHT - 3 * self.game.TILE_SIZE), 45)


    def spawn_enemy(self, pos, start_angle):
        enemy = Enemy(self.game, pos, start_angle, self.player, self.bullets, self.map.wall_positions)
        self.enemies.add(enemy)
