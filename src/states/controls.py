import os

from level.audio import *
from states.state import State


class Controls(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.index = 1

        background_image_path = os.path.join(game.assets_dir, 'background_images', 'Video image 1.png')
        self.background_image = pygame.image.load(background_image_path).convert()
        self.background_image = pygame.transform.scale(self.background_image, (game.WIDTH, game.HEIGHT))

        menu_image_path = os.path.join(game.assets_dir, 'background_images', 'menu.png')
        self.menu_image = pygame.image.load(menu_image_path).convert()
        self.menu_image = pygame.transform.scale(self.menu_image, (672, 768))

        space_bar_path = os.path.join(game.assets_dir, 'background_images', 'SpaceBarImage.png')
        self.space_bar_image = pygame.image.load(space_bar_path).convert()
        self.space_bar_image = pygame.transform.scale(self.space_bar_image, (150, 75))

        esc_path = os.path.join(game.assets_dir, 'background_images', 'ESCKey.png')
        self.esc_image = pygame.image.load(esc_path).convert()
        self.esc_image = pygame.transform.scale(self.esc_image, (150, 75))

        arrow_path = os.path.join(game.assets_dir, 'background_images', 'ArrowKeyImage.png')
        self.up_arrow_image = pygame.image.load(arrow_path).convert()
        self.up_arrow_image = pygame.transform.scale(self.up_arrow_image, (70, 70))

        self.down_arrow_image = pygame.image.load(arrow_path).convert()
        self.down_arrow_image = pygame.transform.scale(self.down_arrow_image, (70, 70))
        self.down_arrow_image = pygame.transform.rotate(self.down_arrow_image, 180)

        self.right_arrow_image = pygame.image.load(arrow_path).convert()
        self.right_arrow_image = pygame.transform.scale(self.right_arrow_image, (70, 70))
        self.right_arrow_image = pygame.transform.rotate(self.right_arrow_image, 270)

        self.left_arrow_image = pygame.image.load(arrow_path).convert()
        self.left_arrow_image = pygame.transform.scale(self.left_arrow_image, (70, 70))
        self.left_arrow_image = pygame.transform.rotate(self.left_arrow_image, 90)

    def update(self, delta_time, actions):
        if actions["space"] or actions["enter"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.background_image, (0, 0))
        display.blit(self.menu_image, (self.game.WIDTH // 2 - 336, self.game.HEIGHT // 2 - 384))

        display.blit(self.space_bar_image, (self.game.WIDTH // 2 - 150 - 15, self.game.HEIGHT // 2 - 285))
        display.blit(self.esc_image, (self.game.WIDTH // 2 + 15, self.game.HEIGHT // 2 - 285))

        display.blit(self.up_arrow_image,
                     (self.game.WIDTH // 2 - 35,
                      self.game.HEIGHT // 2 - 125)
                     )
        display.blit(self.down_arrow_image,
                     (self.game.WIDTH // 2 - 35,
                      self.game.HEIGHT // 2 - 55)
                     )
        display.blit(self.right_arrow_image,
                     (self.game.WIDTH // 2 - 35 + 70,
                      self.game.HEIGHT // 2 - 55)
                     )
        display.blit(self.left_arrow_image,
                     (self.game.WIDTH // 2 - 35 - 70,
                      self.game.HEIGHT // 2 - 55)
                     )

        self.game.draw_controls_text(display, "Shoot/Select",
                                     (255, 255, 255),
                                     self.game.WIDTH / 2 - 89,
                                     self.game.HEIGHT / 2 - 310
                                     )
        self.game.draw_controls_text(display, "Pause",
                                     (255, 255, 255),
                                     self.game.WIDTH / 2 + 90,
                                     self.game.HEIGHT / 2 - 310
                                     )

        self.game.draw_controls_text(display, "Move",
                                     (255, 255, 255),
                                     self.game.WIDTH / 2,
                                     self.game.HEIGHT / 2 - 175
                                     )
        self.game.draw_controls_text(display, "Forward",
                                     (255, 255, 255),
                                     self.game.WIDTH / 2,
                                     self.game.HEIGHT / 2 - 145
                                     )
        self.game.draw_controls_text(display, "Move",
                                     (255, 255, 255),
                                     self.game.WIDTH / 2,
                                     self.game.HEIGHT / 2 + 35
                                     )
        self.game.draw_controls_text(display, "Backward",
                                     (255, 255, 255),
                                     self.game.WIDTH / 2,
                                     self.game.HEIGHT / 2 + 65
                                     )
        self.game.draw_controls_text(display, "Rotate",
                                     (255, 255, 255),
                                     self.game.WIDTH / 2 + 120,
                                     self.game.HEIGHT / 2 - 110
                                     )
        self.game.draw_controls_text(display, "Right",
                                     (255, 255, 255),
                                     self.game.WIDTH / 2 + 120,
                                     self.game.HEIGHT / 2 - 80
                                     )

        self.game.draw_controls_text(display, "Rotate",
                                     (255, 255, 255),
                                     self.game.WIDTH / 2 - 120,
                                     self.game.HEIGHT / 2 - 110
                                     )
        self.game.draw_controls_text(display, "Left",
                                     (255, 255, 255),
                                     self.game.WIDTH / 2 - 120,
                                     self.game.HEIGHT / 2 - 80
                                     )

        self.game.draw_button(display, "Back",
                              (0, 255, 0), (255, 255, 255),
                              self.game.WIDTH // 2 + 65,
                              self.game.HEIGHT // 2 + 100,
                              100, 50
                              )
