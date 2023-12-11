import pygame
import os

from states.state import State


class GameOver(State):
    def __init__(self, game, win):
        State.__init__(self, game)
        self.win = win
        self.index = 1

        background_image_path = os.path.join(game.assets_dir, 'background_images', 'Video image 1.png')
        self.background_image = pygame.image.load(background_image_path).convert()
        self.background_image = pygame.transform.scale(self.background_image, (game.WIDTH, game.HEIGHT))

    def update(self, delta_time, actions):
        if actions["space"] or actions["enter"]:
            if self.index == 1:
                self.exit_state()
            elif self.index == 2:
                self.game.state_stack.pop()
                self.exit_state()
        if actions["up"] & actions["down"]:
            pass
        elif actions["up"] or actions["down"]:
            if self.index == 1:
                self.index = 2
            else:
                self.index = 1
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.background_image, (0, 0))
        #display.fill((255, 255, 255))

        pygame.draw.rect(display, (0, 0, 128),
                         pygame.Rect(self.game.WIDTH // 2 - 200, self.game.HEIGHT // 2 - 250, 400, 500))
        if self.win:
            self.game.draw_text(display, "You Win!", (255, 255, 255), self.game.WIDTH / 2, self.game.HEIGHT / 4)
        else:
            self.game.draw_text(display, "You Lose!", (255, 255, 255), self.game.WIDTH / 2, self.game.HEIGHT / 4)

        if self.index == 1:
            self.game.draw_button(display, "Play Level Again", (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 150,
                                  self.game.HEIGHT // 2 - 100, 300, 75)
            self.game.draw_button(display, "Level Select", (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 125,
                                  self.game.HEIGHT // 2, 250, 75)
        elif self.index == 2:
            self.game.draw_button(display, "Play Level Again", (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 150,
                                  self.game.HEIGHT // 2 - 100, 300, 75)
            self.game.draw_button(display, "Level Select", (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 125,
                                  self.game.HEIGHT // 2, 250, 75)
