import os

from states.level import Level
from states.state import State
from level.audio import *


class LevelSelect(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.index = 1

        background_image_path = os.path.join(game.assets_dir, 'background_images', 'Video image 1.png')
        self.background_image = pygame.image.load(background_image_path).convert()
        self.background_image = pygame.transform.scale(self.background_image, (game.WIDTH, game.HEIGHT))

    def update(self, delta_time, actions):
        if actions["space"] or actions["enter"]:
            if self.index in self.game.levels.keys():
                if self.game.levels[self.index]['status'] == 'unlocked':
                    if self.game.levels[self.index]['level'] == None:
                        self.game.levels[self.index]['level'] = Level(self.game, self.index)
                        new_state = self.game.levels[self.index]['level']
                    else:
                        new_state = self.game.levels[self.index]['level']
                    new_state.enter_state()
                    round_start_sound()    
            else:
                self.exit_state()
        if actions["up"] & actions["down"]:
            pass
        elif actions["up"]:
            next_index = self.index - 1
            if next_index == 0:
                self.index = 4
            else:
                for _ in range(len(self.game.levels)):
                    if self.game.levels[next_index]['status'] == 'locked':
                        next_index -= 1
                        if next_index == 0:
                            self.index = 4
                            break
                    else:
                        self.index = next_index
                        break
        elif actions["down"]:
            next_index = self.index + 1
            if next_index == 4:
                self.index = 4
            elif next_index == 5:
                self.index = 1
            else:
                for _ in range(len(self.game.levels)):
                    if self.game.levels[next_index]['status'] == 'locked':
                        next_index += 1
                        if next_index == 4:
                            self.index = 4
                            break
                        if next_index == 5:
                            self.index = 1
                            break
                    else:
                        self.index = next_index
                        break
        self.game.reset_keys()

    def render(self, display):
        display.blit(self.background_image, (0, 0))

        pygame.draw.rect(display, (0, 0, 128),
                         pygame.Rect(self.game.WIDTH // 2 - 200, self.game.HEIGHT // 2 - 250, 400, 500))
        self.game.draw_text(display, "Level Select", (255, 255, 255), self.game.WIDTH / 2, self.game.HEIGHT / 4)

        for level in self.game.levels.keys():
            if self.game.levels[level]['status'] == 'locked':
                self.game.draw_button(display, f"Level {level}", (128, 128, 128), (255, 255, 255),
                                      self.game.WIDTH // 2 - 125,
                                      self.game.HEIGHT // 2 - 150 + (100 * (level - 1)), 250, 75)
            elif level == self.index:
                self.game.draw_button(display, f"Level {level}", (0, 255, 0), (255, 255, 255),
                                      self.game.WIDTH // 2 - 125,
                                      self.game.HEIGHT // 2 - 150 + (100 * (level - 1)), 250, 75)
            else:
                self.game.draw_button(display, f"Level {level}", (255, 0, 0), (255, 255, 255),
                                      self.game.WIDTH // 2 - 125,
                                      self.game.HEIGHT // 2 - 150 + (100 * (level - 1)), 250, 75)
        if self.index == 4:
            self.game.draw_button(display, "Back", (0, 255, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 125,
                                  self.game.HEIGHT // 2 - 150 + (100 * 3), 250, 75)
        else:
            self.game.draw_button(display, "Back", (255, 0, 0), (255, 255, 255),
                                  self.game.WIDTH // 2 - 125,
                                  self.game.HEIGHT // 2 - 150 + (100 * 3), 250, 75)
