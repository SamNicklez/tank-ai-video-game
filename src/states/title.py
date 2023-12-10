import sys

import pygame

from states.level_select import LevelSelect
from states.state import State


class Title(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.menu_options = {0: "level_select", 1: "controls", 2: "quit"}
        self.index = 0

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
        display.fill((255, 255, 255))

        pygame.draw.rect(display, (0, 0, 128),
                         pygame.Rect(self.game.WIDTH // 2 - 200, self.game.HEIGHT // 2 - 250, 400, 500))
        self.game.draw_text(display, "GAIT Tanks", (255, 255, 255), self.game.WIDTH / 2, self.game.HEIGHT / 4)

        if self.menu_options[self.index] == 'level_select':
            self.game.draw_button(display, "Level Select", (0, 255, 0), (255, 255, 255), self.game.WIDTH // 2 - 125,
                                  self.game.HEIGHT // 2 - 100, 250, 75)
            self.game.draw_button(display, "Controls", (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 125, self.game.HEIGHT // 2, 250, 75)
            self.game.draw_button(display, "Quit", (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 125, self.game.HEIGHT // 2 + 100, 250, 75)
        elif self.menu_options[self.index] == 'controls':
            self.game.draw_button(display, "Level Select", (255, 0, 0), (255, 255, 255), self.game.WIDTH // 2 - 125,
                                  self.game.HEIGHT // 2 - 100, 250, 75)
            self.game.draw_button(display, "Controls", (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 125, self.game.HEIGHT // 2, 250, 75)
            self.game.draw_button(display, "Quit", (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 125, self.game.HEIGHT // 2 + 100, 250, 75)
        elif self.menu_options[self.index] == 'quit':
            self.game.draw_button(display, "Level Select", (255, 0, 0), (255, 255, 255), self.game.WIDTH // 2 - 125,
                                  self.game.HEIGHT // 2 - 100, 250, 75)
            self.game.draw_button(display, "Controls", (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 125, self.game.HEIGHT // 2, 250, 75)
            self.game.draw_button(display, "Quit", (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 125, self.game.HEIGHT // 2 + 100, 250, 75)
