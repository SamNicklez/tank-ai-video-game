import pygame

from player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        self.clock = pygame.time.Clock()
        self.player = Player(self.screen)
        self.bullets = pygame.sprite.Group()
        self.running = True

    def run(self):
        while self.running:
            pressed_keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot(self.bullets)

            # Update game objects
            self.player.update(pressed_keys)
            self.bullets.update()

            # Draw everything
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.player.image, self.player.rect)
            self.bullets.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()