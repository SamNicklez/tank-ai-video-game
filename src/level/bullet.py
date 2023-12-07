import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, walls, start_pos, start_angle):
        super(Bullet, self).__init__()
        self.game = game
        self.walls = walls
        self.original_image = pygame.image.load(f"{game.sprite_dir}/bullet.png").convert_alpha()
        self.angle = start_angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = pygame.math.Vector2(0, -1).rotate(-self.angle)
        self.rect = self.image.get_rect(center=(start_pos + self.direction))
        self.speed = 10

    def update(self, player, enemies):
        new_position = self.rect.copy()
        new_position.move_ip(self.direction * self.speed)

        if not self.check_collisions(new_position):
            if self.game.screen.get_rect().contains(self.rect):
                self.rect = new_position
            else:
                self.kill()
        else:
            self.kill()

        hit_enemies = pygame.sprite.spritecollide(self, enemies, True, pygame.sprite.collide_mask)
        hit_player = pygame.sprite.spritecollide(self, [player], False, pygame.sprite.collide_mask)
        if hit_enemies or hit_player:
            self.kill()
            if hit_player:
                player.health -= 1

    def check_collisions(self, new_rect):
        for wall in self.walls:
            if new_rect.colliderect(wall):
                return True
        return False
