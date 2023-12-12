import os

from states.level import Level
from states.state import State
from level.audio import *


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
        self.up_arrow_image = pygame.transform.scale(self.up_arrow_image, (75, 75))

        self.down_arrow_image = pygame.image.load(arrow_path).convert()
        self.down_arrow_image = pygame.transform.scale(self.down_arrow_image, (75, 75))

        self.right_arrow_image = pygame.image.load(arrow_path).convert()
        self.right_arrow_image = pygame.transform.scale(self.right_arrow_image, (75, 75))

        arrow_path = os.path.join(game.assets_dir, 'background_images', 'ArrowKeyImage.png')
        self.left_arrow_image = pygame.image.load(arrow_path).convert()
        self.left_arrow_image = pygame.transform.scale(self.left_arrow_image, (75, 75))


    def update(self, delta_time, actions):
        if actions["space"] or actions["enter"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.background_image, (0, 0))
        display.blit(self.menu_image, (self.game.WIDTH // 2 - 336, self.game.HEIGHT // 2 - 384))

        display.blit(self.space_bar_image, (self.game.WIDTH // 2 - 150 - 15, self.game.HEIGHT // 2 - 285))

        display.blit(self.esc_image, (self.game.WIDTH // 2 + 15, self.game.HEIGHT // 2 - 285))
    
        display.blit(self.up_arrow_image, (self.game.WIDTH // 2 - 150, self.game.HEIGHT // 2 - 50))

        #self.game.draw_text(display, "GAIT Tanks", (255, 255, 255), self.game.WIDTH / 2, self.game.HEIGHT / 2 - 290)

        self.game.draw_controls_text(display, "Shoot/Select", (255, 255, 255), self.game.WIDTH / 2 - 89, self.game.HEIGHT / 2 - 310)
        self.game.draw_controls_text(display, "Pause", (255, 255, 255), self.game.WIDTH / 2 + 90, self.game.HEIGHT / 2 - 310)
        #self.game.draw_text(display, "GAIT Tanks", (255, 255, 255), self.game.WIDTH / 2, self.game.HEIGHT / 2 - 290)

        self.game.draw_button(display, "Back",
                                  (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 + 65,
                                  self.game.HEIGHT // 2 + 100,
                                  100, 50
                                  )

        