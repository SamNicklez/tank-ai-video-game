import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, start_pos, direction):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.Surface((5, 5))  # Bullet size
        self.image.fill((255, 255, 255))  # Bullet color (white)
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = 10  # Bullet speed
        self.direction = direction

    def update(self):
        self.rect.move_ip(self.direction * self.speed)
        # Remove the bullet if it goes off-screen
        if not self.screen.get_rect().contains(self.rect):
            self.kill()