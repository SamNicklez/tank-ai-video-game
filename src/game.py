import pygame

from enemy import Enemy
from map import Map
from player import Player

WIDTH = 1280
HEIGHT = 720
TILE_SIZE = 16


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
        self.player = Player(self.screen, (300, 360), self.bullets, self.map.wall_positions)
        self.spawn_enemy(pos=(900, 360))

        while self.running:
            if len(self.enemies) < 1:
                self.spawn_enemy(pos=(900, 360))
            if self.player.health <= 0:
                self.running = False
            current_time = pygame.time.get_ticks()
            self.screen.fill((0, 0, 0))
            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update game objects
            self.player.update(pressed_keys, current_time)
            self.enemies.update(current_time)
            self.bullets.update()

            self.check_bullet_collisions()

            # Draw everything
            self.screen.blit(self.map.background, (0, 0))
            self.player.draw(self.screen)
            self.enemies.draw(self.screen)
            self.bullets.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

    def spawn_enemy(self, pos=(100, 100)):
        enemy = Enemy(self.screen, pos, self.player, self.bullets, self.map.wall_positions)  # Pass bullets group to enemy
        self.enemies.add(enemy)

    def check_bullet_collisions(self):
        for bullet in self.bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, self.enemies, True, pygame.sprite.collide_mask)
            hit_player = pygame.sprite.spritecollide(bullet, [self.player], False, pygame.sprite.collide_mask)
            if hit_enemies or hit_player:
                bullet.kill()
            if hit_player:
                self.player.health -= 1
