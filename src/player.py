import pygame

from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        self.screen = screen
        self.hull_image = pygame.image.load('assets/T-34/hull.png').convert_alpha()
        self.turret_image = pygame.image.load('assets/T-34/turret.png').convert_alpha()

        self.combined_image = pygame.Surface(self.hull_image.get_size(), pygame.SRCALPHA)
        self.combined_image.blit(self.hull_image, (0, 0))

        turret_center = (self.hull_image.get_width() // 2, self.hull_image.get_height() // 2)
        turret_rect = self.turret_image.get_rect(center=turret_center)
        self.combined_image.blit(self.turret_image, turret_rect.topleft)

        self.image = self.combined_image.copy()
        self.rect = self.image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        self.direction = pygame.math.Vector2(0, -1)
        self.angle = 0

        self.PLAYER_SIZE = 50
        self.PLAYER_COLOR = (255, 0, 0)
        self.FORWARD_VELOCITY = 5
        self.BACKWARD_VELOCITY = 2
        self.ROTATION_SPEED = 5

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(self.direction * self.FORWARD_VELOCITY)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(self.direction * -self.BACKWARD_VELOCITY)
        if pressed_keys[pygame.K_LEFT]:
            self.angle += self.ROTATION_SPEED
        if pressed_keys[pygame.K_RIGHT]:
            self.angle -= self.ROTATION_SPEED

        # Update direction
        self.direction = pygame.math.Vector2(0, -1).rotate(-self.angle)

        # Rotate the combined image
        self.image = pygame.transform.rotate(self.combined_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Keep player on the screen
        self.rect.clamp_ip(self.screen.get_rect())

    def draw(self, screen):
        # Rotate the player's surface
        rotated_surf = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_surf.get_rect(center=self.rect.center)
        # Draw rotated surface
        screen.blit(rotated_surf, rotated_rect)

    def shoot(self, bullets_group):
        bullet_start_pos = self.rect.center + self.direction * 40
        new_bullet = Bullet(self.screen, bullet_start_pos, self.direction)
        bullets_group.add(new_bullet)
