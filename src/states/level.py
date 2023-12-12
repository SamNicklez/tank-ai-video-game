from level.audio import *
from level.enemy import Enemy
from level.map import Map
from level.player import Player
from states.game_over import GameOver
from states.pause_menu import PauseMenu
from states.state import State


class Level(State):
    def __init__(self, game, number):
        State.__init__(self, game)
        self.number = number
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.visual_effects = pygame.sprite.Group()
        self.map = Map(self.game, number)
        self.player = None

        self.level_init()

    def update(self, delta_time, actions):
        if len(self.enemies) < 1:
            if self.number < len(self.game.levels):
                self.game.levels[(self.number + 1)]['status'] = 'unlocked'
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
        display.blit(self.map.background_image, (0, 0))
        display.blit(self.map.background, (0, 0))
        # display.blit(self.map.background_image, (0, 0))
        self.player.render(display)
        self.enemies.draw(display)
        self.bullets.draw(display)
        self.visual_effects.draw(display)
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
        self.visual_effects.empty()
        self.map.wall_positions.clear()

        self.map.load_textures()
        self.map.initialize_map_tiles()

        if self.number == 1:
            self.player = Player(
                self.game,
                (4 * self.game.TILE_SIZE, 11 * self.game.TILE_SIZE),
                270,
                self.bullets,
                self.visual_effects,
                self.map.wall_positions
            )

            self.spawn_enemy((
                35 * self.game.TILE_SIZE,
                12 * self.game.TILE_SIZE
            ),
                90
            )
        elif self.number == 2:
            self.player = Player(
                self.game,
                (20 * self.game.TILE_SIZE, 20 * self.game.TILE_SIZE),
                0,
                self.bullets,
                self.visual_effects,
                self.map.wall_positions
            )

            self.spawn_enemy((
                4 * self.game.TILE_SIZE,
                3 * self.game.TILE_SIZE
            ),
                180
            )
            self.spawn_enemy((
                35 * self.game.TILE_SIZE,
                3 * self.game.TILE_SIZE
            ),
                180
            )
        elif self.number == 3:
            self.player = Player(self.game, (5 * self.game.TILE_SIZE, 4 * self.game.TILE_SIZE), 225, self.bullets, self.visual_effects,
                                 self.map.wall_positions)

            self.spawn_enemy((self.game.WIDTH - 5 * self.game.TILE_SIZE, self.game.HEIGHT - 4 * self.game.TILE_SIZE),
                             45)

    def spawn_enemy(self, pos, start_angle):
        enemy = Enemy(self.game, pos, start_angle, self.player, self.bullets, self.visual_effects, self.map.wall_positions)
        self.enemies.add(enemy)
