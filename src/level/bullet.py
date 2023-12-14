import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, walls, start_pos, start_angle, visual_effects_group):
        super(Bullet, self).__init__()
        self.game = game
        self.walls = walls
        self.visual_effects_group = visual_effects_group
        self.original_image = pygame.image.load(fr"{game.sprite_dir}\bullet.png").convert_alpha()
        self.angle = start_angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = pygame.math.Vector2(0, -1).rotate(-self.angle)
        self.rect = self.image.get_rect(center=(start_pos + self.direction))
        self.speed = 10

        self.fire_effect = FireEffect(self, self.game)
        self.visual_effects_group.add(self.fire_effect)

    def update(self, player, enemies):
        new_position = self.rect.copy()
        new_position.move_ip(self.direction * self.speed)

        if not self.check_collisions(new_position):
            if self.game.screen.get_rect().contains(self.rect):
                self.rect = new_position
                self.fire_effect.update()
            else:
                self.kill()
                self.fire_effect.kill()
        else:
            self.kill()
            self.fire_effect.kill()

        hit_enemies = pygame.sprite.spritecollide(self, enemies, True, pygame.sprite.collide_mask)
        hit_player = pygame.sprite.spritecollide(self, [player], False, pygame.sprite.collide_mask)
        if hit_enemies or hit_player:
            self.kill()
            self.fire_effect.kill()
            if hit_player:
                player.health -= 1

    def check_collisions(self, new_rect):
        for wall in self.walls:
            if new_rect.colliderect(wall):
                return True
        return False


class FireEffect(pygame.sprite.Sprite):
    def __init__(self, bullet, game):
        super(FireEffect, self).__init__()
        self.game = game
        self.following_bullet = bullet
        self.original_image1 = pygame.image.load(f"{game.sprite_dir}/fire1.png").convert_alpha()
        self.original_image2 = pygame.image.load(f"{game.sprite_dir}/fire2.png").convert_alpha()
        self.angle = bullet.angle
        self.image = pygame.transform.rotate(self.original_image1, self.angle)
        self.direction = pygame.math.Vector2(0, -1).rotate(-self.angle)
        self.rect = self.image.get_rect(center=(bullet.rect.center - self.direction * 10))

        self.current_image = 1

    def update(self):
        if self.current_image == 1:
            self.image = pygame.transform.rotate(self.original_image2, self.following_bullet.angle)
            self.current_image = 2
        else:
            self.image = pygame.transform.rotate(self.original_image1, self.following_bullet.angle)
            self.current_image = 1
        new_position = self.rect.copy()
        new_position.move_ip(self.direction * self.following_bullet.speed)
        self.rect = new_position
