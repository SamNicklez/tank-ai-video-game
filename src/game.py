import os

import numpy as np
from PIL import Image
from moviepy.editor import VideoFileClip

from level.audio import *
from states.title import Title


class Game:
    def __init__(self):
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)

        # Initialize Pygame and the mixer
        pygame.init()
        pygame.mixer.init()

        self.WIDTH = 1280
        self.HEIGHT = 768
        self.TILE_SIZE = 32
        self.NUM_TILES_WIDTH = self.WIDTH // self.TILE_SIZE
        self.NUM_TILES_HEIGHT = self.HEIGHT // self.TILE_SIZE

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.clock = pygame.time.Clock()
        self.current_time = 0

        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up": False, "down": False, "space": False, "enter": False,
                        "escape": False}
        self.state_stack = []

        self.load_assets()
        self.load_states()

        self.levels = {
            1: {
                'level': None,
                'status': 'unlocked'
            },
            2: {
                'level': None,
                'status': 'unlocked'
            },
            3: {
                'level': None,
                'status': 'unlocked'
            },
        }

    def game_loop(self):
        while self.playing:
            # check if background sound is playing
            if check_background_sound():
                pass
            else:
                game_background_sound()
            self.get_dt()
            self.get_events()
            self.update()
            self.render()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.actions['left'] = True
                if event.key == pygame.K_RIGHT:
                    self.actions['right'] = True
                if event.key == pygame.K_UP:
                    self.actions['up'] = True
                if event.key == pygame.K_DOWN:
                    self.actions['down'] = True
                if event.key == pygame.K_SPACE:
                    self.actions['space'] = True
                if event.key == pygame.K_RETURN:
                    self.actions['enter'] = True
                if event.key == pygame.K_ESCAPE:
                    self.actions['escape'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.actions['left'] = False
                if event.key == pygame.K_RIGHT:
                    self.actions['right'] = False
                if event.key == pygame.K_UP:
                    self.actions['up'] = False
                if event.key == pygame.K_DOWN:
                    self.actions['down'] = False
                if event.key == pygame.K_SPACE:
                    self.actions['space'] = False
                if event.key == pygame.K_RETURN:
                    self.actions['enter'] = False
                if event.key == pygame.K_ESCAPE:
                    self.actions['escape'] = False

    def update(self):
        self.state_stack[-1].update(self.current_time, self.actions)

    def render(self):
        self.state_stack[-1].render(self.screen)
        # Render current state to the screen

        pygame.display.flip()
        self.clock.tick(30)

    def get_dt(self):
        self.current_time = pygame.time.get_ticks()

    def draw_text(self, surface, text, color, x, y):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def draw_button(self, surface, text, button_color, text_color, x, y, width, height, button_width=2,
                    button_height=6):
        button = pygame.Rect(x, y, width, height)
        pygame.draw.rect(surface, button_color, button, button_width, button_height)
        text_surface = self.font_button.render(text, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = button.center
        surface.blit(text_surface, text_rect)
        return button

    def draw_button_color(self, surface, button, button_color):
        pygame.draw.rect(surface, button_color, button)

    def load_assets(self):
        # Create pointers to directories
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.font = pygame.font.Font(self.assets_dir + "/fonts/Blockletter.otf", 70)
        self.font_button = pygame.font.Font(self.assets_dir + "/fonts/Blockletter.otf", 42)
        self.title_font = pygame.font.Font(self.assets_dir + "/fonts/Blockletter.otf", 120)
        # Load all sounds
        load_sounds()

    def load_states(self):
        self.title_screen = Title(self)
        self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def intro(self):
        # Function to resize each frame of the video
        def resize_frame(frame):
            pil_image = Image.fromarray(frame)
            resized_image = pil_image.resize((self.WIDTH, self.HEIGHT), Image.Resampling.LANCZOS)
            return np.array(resized_image)

        # Load the video
        intro_clip = VideoFileClip(os.path.join(self.assets_dir, 'videos/intro_video2.mp4')).without_audio()

        audio_path = os.path.join(self.assets_dir, "audio/intro_video_audio.mp3")

        # Initialize Pygame mixer and play the audio
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        # Resize each frame
        resized_clip = intro_clip.fl_image(resize_frame)

        # Play the resized video
        resized_clip.preview()

        # Close the clip after playing
        resized_clip.close()
        pygame.mixer.music.stop()


if __name__ == "__main__":

    g = Game()
    while g.running:
        g.game_loop()
