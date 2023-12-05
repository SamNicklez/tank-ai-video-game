from time import sleep

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
        self.player = None
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.running = True
        self.map = Map(WIDTH, HEIGHT, TILE_SIZE)

    def run(self):
        self.map.load_textures()
        self.map.initialize_map_tiles()
        self.player = Player(self.screen, (4*TILE_SIZE, 3*TILE_SIZE), 225, self.bullets, self.map.wall_positions)
        self.spawn_enemy((WIDTH - 4*TILE_SIZE, HEIGHT - 3*TILE_SIZE), 45)

        self.update(pygame.key.get_pressed(), pygame.time.get_ticks())
        self.draw()
        pygame.display.flip()
        self.clock.tick(30)
        sleep(2)

        while self.running:
            if len(self.enemies) < 1:
                self.spawn_enemy((1150, HEIGHT // 2), 45)
            if self.player.health <= 0:
                self.running = False

            current_time = pygame.time.get_ticks()
            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update game objects
            self.update(pressed_keys, current_time)

            # Draw everything
            self.draw()

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

    def update(self, pressed_keys, current_time):
        # Update game objects
        self.player.update(pressed_keys, current_time)
        self.enemies.update(current_time)
        self.bullets.update()
        self.check_bullet_collisions()

    def draw(self):
        # Draw everything
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.map.background, (0, 0))
        self.player.draw(self.screen)
        self.enemies.draw(self.screen)
        self.bullets.draw(self.screen)

    def spawn_enemy(self, pos, start_angle):
        enemy = Enemy(self.screen, pos, start_angle, self.player, self.bullets, self.map.wall_positions)  # Pass bullets group to enemy
        self.enemies.add(enemy)

    def check_bullet_collisions(self):
        for bullet in self.bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, self.enemies, True, pygame.sprite.collide_mask)
            hit_player = pygame.sprite.spritecollide(bullet, [self.player], False, pygame.sprite.collide_mask)
            if hit_enemies or hit_player:
                bullet.kill()
            if hit_player:
                self.player.health -= 1
