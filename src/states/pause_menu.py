import os

import pygame

from states.state import State


class PauseMenu(State):
    def __init__(self, game, level):
        State.__init__(self, game)
        self.level = level

        self.menu_options = {0: "resume", 1: "restart", 2: "controls", 3: "level_select"}
        self.index = 0

        menu_image_path = os.path.join(game.assets_dir, 'background_images', 'menu.png')
        self.menu_image = pygame.image.load(menu_image_path).convert()
        self.menu_image = pygame.transform.scale(self.menu_image, (672, 768))

    def update(self, delta_time, actions):
        if actions["space"] or actions["enter"]:
            if self.index == 0:
                self.exit_state()
            elif self.index == 1:
                self.level.level_init()
                self.exit_state()
            elif self.index == 2:
                pass
            elif self.index == 3:
                self.level.level_init()
                self.game.state_stack.pop()
                self.exit_state()
        if actions["up"] & actions["down"]:
            pass
        elif actions["up"]:
            if self.menu_options[self.index] == 'resume':
                self.index = 3
            elif self.menu_options[self.index] == 'restart':
                self.index = 0
            elif self.menu_options[self.index] == 'controls':
                self.index = 1
            elif self.menu_options[self.index] == 'level_select':
                self.index = 2
        elif actions["down"]:
            if self.menu_options[self.index] == 'resume':
                self.index = 1
            elif self.menu_options[self.index] == 'restart':
                self.index = 2
            elif self.menu_options[self.index] == 'controls':
                self.index = 3
            elif self.menu_options[self.index] == 'level_select':
                self.index = 0
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.menu_image, (self.game.WIDTH // 2 - 336, self.game.HEIGHT // 2 - 384))

        self.game.draw_text(display, "Pause Menu", (255, 255, 255), self.game.WIDTH // 2, self.game.HEIGHT // 2 - 290)

        if self.menu_options[self.index] == 'resume':
            self.game.draw_button(display, "Resume",
                                  (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 240,
                                  260, 75
                                  )
            self.game.draw_button(display, "Restart",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 140,
                                  260, 75
                                  )
            self.game.draw_button(display, "Controls",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 40,
                                  260, 75
                                  )
            self.game.draw_button(display, "Level Select",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 + 60,
                                  260, 75
                                  )
        elif self.menu_options[self.index] == 'restart':
            self.game.draw_button(display, "Resume",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 240,
                                  260, 75
                                  )
            self.game.draw_button(display, "Restart",
                                  (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 140,
                                  260, 75
                                  )
            self.game.draw_button(display, "Controls",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 40,
                                  260, 75
                                  )
            self.game.draw_button(display, "Level Select",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 + 60,
                                  260, 75
                                  )
        elif self.menu_options[self.index] == 'controls':
            self.game.draw_button(display, "Resume",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 240,
                                  260, 75
                                  )
            self.game.draw_button(display, "Restart",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 140,
                                  260, 75
                                  )
            self.game.draw_button(display, "Controls",
                                  (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 40,
                                  260, 75
                                  )
            self.game.draw_button(display, "Level Select",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 + 60,
                                  260, 75
                                  )
        elif self.menu_options[self.index] == 'level_select':
            self.game.draw_button(display, "Resume",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 240,
                                  260, 75
                                  )
            self.game.draw_button(display, "Restart",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 140,
                                  260, 75
                                  )
            self.game.draw_button(display, "Controls",
                                  (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 - 40,
                                  260, 75
                                  )
            self.game.draw_button(display, "Level Select",
                                  (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 130,
                                  self.game.HEIGHT // 2 + 60,
                                  260, 75
                                  )
