import os
import sys

import pygame

from states.level_select import LevelSelect
from states.state import State


class Title(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.menu_options = {0: "level_select", 1: "controls", 2: "quit"}
        self.index = 0

        background_image_path = os.path.join(game.assets_dir, 'background_images', 'Video image 1.png')
        self.background_image = pygame.image.load(background_image_path).convert()
        self.background_image = pygame.transform.scale(self.background_image, (game.WIDTH, game.HEIGHT))
        menu_image_path = os.path.join(game.assets_dir, 'background_images', 'menu.png')
        self.menu_image = pygame.image.load(menu_image_path).convert()
        self.menu_image = pygame.transform.scale(self.menu_image, (672, 768))

    def update(self, delta_time, actions):
        if actions["space"] or actions["enter"]:
            if self.menu_options[self.index] == 'level_select':
                new_state = LevelSelect(self.game)
                new_state.enter_state()
            elif self.menu_options[self.index] == 'controls':
                pass
            elif self.menu_options[self.index] == 'quit':
                pygame.quit()
                sys.exit()
        if actions["up"] & actions["down"]:
            pass
        elif actions["up"]:
            if self.menu_options[self.index] == 'level_select':
                self.index = 2
            elif self.menu_options[self.index] == 'controls':
                self.index = 0
            elif self.menu_options[self.index] == 'quit':
                self.index = 1
        elif actions["down"]:
            if self.menu_options[self.index] == 'level_select':
                self.index = 1
            elif self.menu_options[self.index] == 'controls':
                self.index = 2
            elif self.menu_options[self.index] == 'quit':
                self.index = 0
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.background_image, (0, 0))
        display.blit(self.menu_image, (self.game.WIDTH // 2 - 336, self.game.HEIGHT // 2 - 384))

        self.game.draw_text(display, "GAIT Tanks", (255, 255, 255), self.game.WIDTH / 2, self.game.HEIGHT / 2 - 290)

        if self.menu_options[self.index] == 'level_select':
            self.game.draw_button(display, "Level Select",
                                  (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 200,
                                  260, 75
                                  )
            self.game.draw_button(display, "Controls",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 75,
                                  260, 75
                                  )
            self.game.draw_button(display, "Quit",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 + 50,
                                  260, 75
                                  )
        elif self.menu_options[self.index] == 'controls':
            self.game.draw_button(display, "Level Select",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 200,
                                  260, 75
                                  )
            self.game.draw_button(display, "Controls",
                                  (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 75,
                                  260, 75
                                  )
            self.game.draw_button(display, "Quit",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 + 50,
                                  260, 75
                                  )
        elif self.menu_options[self.index] == 'quit':
            self.game.draw_button(display, "Level Select",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 200,
                                  260, 75
                                  )
            self.game.draw_button(display, "Controls",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 75,
                                  260, 75
                                  )
            self.game.draw_button(display, "Quit",
                                  (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 + 50,
                                  260, 75
                                  )
