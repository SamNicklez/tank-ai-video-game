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

    def update(self, delta_time, actions):
        if actions["space"] or actions["enter"]:
            self.exit_state()
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.background_image, (0, 0))

        