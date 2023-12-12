import pygame
import os

from PIL import Image
import numpy as np

from moviepy.editor import VideoFileClip

from states.state import State
from level.audio import *

class GameOver(State):
    def __init__(self, game, win):
        State.__init__(self, game)
        self.win = win
        self.index = 1

        background_image_path = os.path.join(game.assets_dir, 'background_images', 'Video image 1.png')
        self.background_image = pygame.image.load(background_image_path).convert()
        self.background_image = pygame.transform.scale(self.background_image, (game.WIDTH, game.HEIGHT))

        menu_image_path = os.path.join(game.assets_dir, 'background_images', 'menu.png')
        self.menu_image = pygame.image.load(menu_image_path).convert()
        self.menu_image = pygame.transform.scale(self.menu_image, (672, 768))

        # play the level completed clip
        if win:
            you_won_sound()
            self.play_video(self.game)
        else:
            you_lost_sound() 
            self.play_video(self.game)
        

    def play_video(self, game):

        if self.win:
            path = "videos/level_completed_video.mp4"
        else:
            path = "videos/level_failed_video.mp4"

        # Function to resize each frame of the video
        def resize_frame(frame):
            pil_image = Image.fromarray(frame)
            resized_image = pil_image.resize((game.WIDTH, game.HEIGHT), Image.Resampling.LANCZOS)
            return np.array(resized_image)

        # Load the video
        intro_clip = VideoFileClip(os.path.join(game.assets_dir, path)).without_audio()

        # Resize each frame
        resized_clip = intro_clip.fl_image(resize_frame)

        # Play the resized video
        resized_clip.preview()

        # Close the clip after playing
        resized_clip.close()


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
        display.blit(self.menu_image, (self.game.WIDTH // 2 - 336, self.game.HEIGHT // 2 - 384))

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
