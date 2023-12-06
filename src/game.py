import sys

import pygame

from enemy import Enemy
from map import Map
from player import Player

WIDTH = 1280
HEIGHT = 768
TILE_SIZE = 32


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        self.current_level = None
        self.levels = {
            1: {
                'assets': 'assets/map/',
                'status': 'unlocked',
            },
            2: {
                'assets': 'assets/map/',
                'status': 'locked',
            },
            3: {
                'assets': 'assets/map/',
                'status': 'locked',
            }
        }
        self.player = None
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.running = True
        self.map = Map(WIDTH, HEIGHT, TILE_SIZE)

        self.title_font = pygame.font.Font(None, 72)
        self.button_font = pygame.font.Font(None, 50)

    def run(self):
        while True:
            self.main_menu()
            self.level_start()

    def main_menu(self):
        menu = True
        play_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 20, 200, 40)

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.collidepoint(event.pos):
                        menu = False

            self.screen.fill((0, 0, 0))  # Background color
            title_text = self.title_font.render("Tank Game", True, (255, 255, 255))
            play_text = self.button_font.render("Play", True, (255, 255, 255))

            title_text_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
            self.screen.blit(title_text, title_text_rect)

            pygame.draw.rect(self.screen, (255, 0, 0), play_button)  # Draw play button
            play_text_rect = play_text.get_rect(center=play_button.center)
            self.screen.blit(play_text, play_text_rect)

            pygame.display.flip()
            self.clock.tick(30)

    def level_start(self):
        self.level_init()

        while self.running:
            if len(self.enemies) < 1:
                self.game_over(True)
                return True
            if self.player.health <= 0:
                self.game_over(False)
                return False

            current_time = pygame.time.get_ticks()
            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            # Update game objects
            self.update(pressed_keys, current_time)

            # Draw everything
            self.draw()

            pygame.display.flip()
            self.clock.tick(30)

    def level_init(self):
        self.enemies.empty()
        self.bullets.empty()
        self.map.wall_positions.clear()

        self.map.load_textures()
        self.map.initialize_map_tiles()
        self.player = Player(self.screen, (4 * TILE_SIZE, 3 * TILE_SIZE), 225, self.bullets, self.map.wall_positions)
        self.spawn_enemy((WIDTH - 4 * TILE_SIZE, HEIGHT - 3 * TILE_SIZE), 45)

    def game_over(self, win):
        self.enemies.empty()
        self.bullets.empty()
        self.map.wall_positions.clear()

        game_over = True
        main_menu_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 20, 200, 40)  # Example play button rectangle

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if main_menu_button.collidepoint(event.pos):
                        game_over = False

            self.screen.fill((0, 0, 0))  # Background color
            if win:
                game_over_text = self.title_font.render("You Win!", True, (255, 255, 255))
            else:
                game_over_text = self.title_font.render("You Lose!", True, (255, 255, 255))
            main_menu_text = self.button_font.render("Main Menu", True, (255, 255, 255))

            game_over_text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
            self.screen.blit(game_over_text, game_over_text_rect)

            pygame.draw.rect(self.screen, (255, 0, 0), main_menu_button)  # Draw play button
            play_text_rect = main_menu_text.get_rect(center=main_menu_button.center)
            self.screen.blit(main_menu_text, play_text_rect)

            pygame.display.flip()
            self.clock.tick(30)

    def update(self, pressed_keys, current_time):
        # Update game objects
        self.player.update(pressed_keys, current_time)
        self.enemies.update(current_time)
        self.bullets.update(self.player, self.enemies)

    def draw(self):
        # Draw everything
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.map.background, (0, 0))
        self.player.draw(self.screen)
        self.enemies.draw(self.screen)
        self.bullets.draw(self.screen)

    def spawn_enemy(self, pos, start_angle):
        enemy = Enemy(self.screen, pos, start_angle, self.player, self.bullets,
                      self.map.wall_positions)  # Pass bullets group to enemy
        self.enemies.add(enemy)
