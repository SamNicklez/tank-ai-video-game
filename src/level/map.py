import os
import sys

import pygame


class Map:
    def __init__(self, game, number):
        self.game = game
        self.number = number

        background_image_path = resource_path(os.path.join(game.assets_dir, "background_images", "Partial Floor.png"))
        self.background_image = pygame.image.load(background_image_path).convert()
        self.background_image = pygame.transform.scale(self.background_image, (game.WIDTH, game.HEIGHT))

        self.background = pygame.Surface((self.game.WIDTH, self.game.HEIGHT), pygame.SRCALPHA)

        self.tiles = [[None for _ in range(self.game.WIDTH // self.game.TILE_SIZE)] for _ in
                      range(self.game.HEIGHT // self.game.TILE_SIZE)]
        self.wall_positions = []

        self.out_of_bounds_texture = None
        self.wall_textures = {
            'vert': None,
            'hori': None,
            't': {
                'up': None,
                'down': None,
                'left': None,
                'right': None
            },
            'corner': {
                'up_left': None,
                'up_right': None,
                'down_left': None,
                'down_right': None
            }
        }

    def set_tile(self, x, y, tile_type):

        main_type = tile_type.split(',')
        if 0 <= x < self.game.NUM_TILES_WIDTH and 0 <= y < self.game.NUM_TILES_HEIGHT:
            self.tiles[y][x] = tile_type
            if main_type[0] == 'out_of_bounds':
                self.background.blit(self.out_of_bounds_texture, (x * self.game.TILE_SIZE, y * self.game.TILE_SIZE))
            else:
                self.wall_positions.append(
                    pygame.Rect(x * self.game.TILE_SIZE, y * self.game.TILE_SIZE, self.game.TILE_SIZE,
                                self.game.TILE_SIZE))
                if main_type[0] == 'vert' or main_type[0] == 'hori':
                    self.background.blit(self.wall_textures[main_type[0]],
                                         (x * self.game.TILE_SIZE, y * self.game.TILE_SIZE))
                elif main_type[0] == 't' or main_type[0] == 'corner':
                    self.background.blit(self.wall_textures[main_type[0]][main_type[1]],
                                         (x * self.game.TILE_SIZE, y * self.game.TILE_SIZE))

    def initialize_map_tiles(self):
        self.perimeter()
        if self.number == 1:
            self.map_wall_1()
        elif self.number == 2:
            self.map_wall_2()
        elif self.number == 3:
            self.map_wall_3()

    def perimeter(self):
        for i in range(self.game.NUM_TILES_WIDTH):
            for j in range(self.game.NUM_TILES_HEIGHT):
                if (i < 2) or (i > (self.game.NUM_TILES_WIDTH - 3)) or (j < 1) or (
                        j > (self.game.NUM_TILES_HEIGHT - 2)):
                    self.set_tile(i, j, "out_of_bounds")
                pass

        for i in range(2, self.game.NUM_TILES_WIDTH - 2):
            for j in range(1, self.game.NUM_TILES_HEIGHT - 1):
                if i == 2 or i == self.game.NUM_TILES_WIDTH - 3:
                    self.set_tile(i, j, "vert")
                elif j == 1 or j == self.game.NUM_TILES_HEIGHT - 2:
                    self.set_tile(i, j, "hori")

        self.set_tile(2, 1, "corner,down_right")
        self.set_tile(self.game.NUM_TILES_WIDTH - 3, 1, "corner,down_left")
        self.set_tile(2, self.game.NUM_TILES_HEIGHT - 2, "corner,up_right")
        self.set_tile(self.game.NUM_TILES_WIDTH - 3, self.game.NUM_TILES_HEIGHT - 2, "corner,up_left")

    def map_wall_1(self):
        # All chained horizontal walls
        for i in range(12, 27):
            self.set_tile(i, 6, "hori")
            self.set_tile(i, 17, "hori")
        for i in range(19, 21):
            self.set_tile(i, 10, "hori")
            self.set_tile(i, 13, "hori")

        # All chained vertical walls
        for j in range(7, 10):
            self.set_tile(12, j, "vert")
            self.set_tile(27, j, "vert")
        for j in range(14, 17):
            self.set_tile(12, j, "vert")
            self.set_tile(27, j, "vert")
        for j in range(11, 13):
            self.set_tile(18, j, "vert")
            self.set_tile(21, j, "vert")

        # Corners on chained outer walls
        self.set_tile(12, 6, "corner,down_right")
        self.set_tile(27, 6, "corner,down_left")
        self.set_tile(12, 17, "corner,up_right")
        self.set_tile(27, 17, "corner,up_left")

        # Corners on chained inner walls
        self.set_tile(18, 10, "corner,down_right")
        self.set_tile(21, 10, "corner,down_left")
        self.set_tile(18, 13, "corner,up_right")
        self.set_tile(21, 13, "corner,up_left")

        # Left 2x2 boxes
        self.draw_2x2_box(6, 5)
        self.draw_2x2_box(7, 11)
        self.draw_2x2_box(6, 17)

        # Right 2x2 boxes
        self.draw_2x2_box(32, 5)
        self.draw_2x2_box(31, 11)
        self.draw_2x2_box(32, 17)

    def map_wall_2(self):
        # All chained horizontal walls
        for i in range(7, 18):
            self.set_tile(i, 4, "hori")
            self.set_tile(i, 19, "hori")
        for i in range(22, 33):
            self.set_tile(i, 4, "hori")
            self.set_tile(i, 19, "hori")
        for i in range(11, 19):
            self.set_tile(i, 7, "hori")
            self.set_tile(i, 16, "hori")
        for i in range(21, 29):
            self.set_tile(i, 7, "hori")
            self.set_tile(i, 16, "hori")

        # All chained vertical walls
        for j in range(5, 10):
            self.set_tile(6, j, "vert")
            self.set_tile(33, j, "vert")
        for j in range(14, 19):
            self.set_tile(6, j, "vert")
            self.set_tile(33, j, "vert")
        for j in range(8, 11):
            self.set_tile(10, j, "vert")
            self.set_tile(29, j, "vert")
        for j in range(13, 16):
            self.set_tile(10, j, "vert")
            self.set_tile(29, j, "vert")

        for j in range(10, 14):
            self.set_tile(15, j, "vert")
            self.set_tile(24, j, "vert")

        # Corners on chained outer walls
        self.set_tile(6, 4, "corner,down_right")
        self.set_tile(33, 4, "corner,down_left")
        self.set_tile(6, 19, "corner,up_right")
        self.set_tile(33, 19, "corner,up_left")

        # Corners on chained inner walls
        self.set_tile(10, 7, "corner,down_right")
        self.set_tile(29, 7, "corner,down_left")
        self.set_tile(10, 16, "corner,up_right")
        self.set_tile(29, 16, "corner,up_left")

        # 2x2 box
        self.draw_2x2_box(19, 11)

    def map_wall_3(self):
        # All chained horizontal walls
        for i in range(3, 9):
            self.set_tile(i, 4, "hori")
        for i in range(25, 30):
            self.set_tile(i, 4, "hori")
        for i in range(7, 15):
            self.set_tile(i, 10, "hori")
        for i in range(6, 16):
            self.set_tile(i, 13, "hori")
        for i in range(15, 21):
            self.set_tile(i, 16, "hori")
        for i in range(13, 16):
            self.set_tile(i, 19, "hori")
        for i in range(3, 6):
            self.set_tile(i, 16, "hori")
        for i in range(21, 24):
            self.set_tile(i, 19, "hori")
        for i in range(25, 30):
            self.set_tile(i, 16, "hori")
        for i in range(34, 37):
            self.set_tile(i, 16, "hori")
        for i in range(27, 30):
            self.set_tile(i, 7, "hori")
        for i in range(25, 31):
            self.set_tile(i, 10, "hori")
        for i in range(30, 33):
            self.set_tile(i, 13, "hori")
        for i in range(10, 13):
            self.set_tile(i, 7, "hori")
        for i in range(22, 25):
            self.set_tile(i, 13, "hori")

        # All chained vertical walls
        for j in range(2, 5):
            self.set_tile(12, j, "vert")
            self.set_tile(18, j, "vert")
        for j in range(5, 7):
            self.set_tile(9, j, "vert")
        for j in range(4, 10):
            self.set_tile(15, j, "vert")
        for j in range(5, 11):
            self.set_tile(21, j, "vert")
        for j in range(5, 10):
            self.set_tile(24, j, "vert")
        for j in range(5, 7):
            self.set_tile(30, j, "vert")
        for j in range(4, 13):
            self.set_tile(33, j, "vert")
        for j in range(8, 14):
            self.set_tile(18, j, "vert")
        for j in range(7, 10):
            self.set_tile(6, j, "vert")
        for j in range(17, 20):
            self.set_tile(6, j, "vert")
        for j in range(16, 22):
            self.set_tile(9, j, "vert")
        for j in range(14, 19):
            self.set_tile(12, j, "vert")
        for j in range(17, 20):
            self.set_tile(18, j, "vert")
        for j in range(14, 16):
            self.set_tile(21, j, "vert")
        for j in range(17, 19):
            self.set_tile(24, j, "vert")
        for j in range(17, 20):
            self.set_tile(30, j, "vert")
            self.set_tile(33, j, "vert")
        for j in range(13, 16):
            self.set_tile(27, j, "vert")
        for j in range(19, 22):
            self.set_tile(27, j, "vert")

        # Corners on chained outer walls
        self.set_tile(9, 4, "corner,down_left")
        self.set_tile(9, 7, "corner,up_right")
        self.set_tile(6, 10, "corner,up_right")
        self.set_tile(6, 16, "corner,down_left")
        self.set_tile(12, 19, "corner,up_right")
        self.set_tile(15, 10, "corner,up_left")
        self.set_tile(21, 16, "corner,up_left")
        self.set_tile(21, 13, "corner,down_right")
        self.set_tile(24, 4, "corner,down_right")
        self.set_tile(24, 10, "corner,up_right")
        self.set_tile(24, 16, "corner,down_right")
        self.set_tile(24, 19, "corner,up_left")
        self.set_tile(30, 4, "corner,down_left")
        self.set_tile(30, 7, "corner,up_left")
        self.set_tile(30, 16, "corner,down_left")
        self.set_tile(33, 13, "corner,up_left")
        self.set_tile(33, 16, "corner,down_right")

        # T's on chained inner walls
        self.set_tile(12, 1, "t,down")
        self.set_tile(18, 1, "t,down")
        self.set_tile(12, 13, "t,down")
        self.set_tile(18, 16, "t,down")
        self.set_tile(27, 16, "t,up")
        self.set_tile(27, 22, "t,up")
        self.set_tile(9, 22, "t,up")
        self.set_tile(2, 4, "t,right")
        self.set_tile(2, 16, "t,right")
        self.set_tile(37, 16, "t,left")

    def draw_2x2_box(self, x, y):
        self.set_tile(x, y, "corner,down_right")
        self.set_tile(x + 1, y, "corner,down_left")
        self.set_tile(x, y + 1, "corner,up_right")
        self.set_tile(x + 1, y + 1, "corner,up_left")

    def load_textures(self):
        grass = pygame.image.load(os.path.join(self.game.assets_dir, "map", "grass.png"))
        wall = pygame.image.load(os.path.join(self.game.assets_dir, "map", "wall.png"))
        wall_t = pygame.image.load(os.path.join(self.game.assets_dir, "map", "wall_t.png"))
        wall_corner = pygame.image.load(os.path.join(self.game.assets_dir, "map", "wall_corner.png"))

        wall_textures = {
            'vert': wall,
            'hori': pygame.transform.rotate(wall, 90),
            't': {
                'up': wall_t,
                'down': pygame.transform.rotate(wall_t, 180),
                'left': pygame.transform.rotate(wall_t, 90),
                'right': pygame.transform.rotate(wall_t, 270),
            },
            'corner': {
                'up_left': pygame.transform.rotate(wall_corner, 90),
                'up_right': wall_corner,
                'down_left': pygame.transform.rotate(wall_corner, 180),
                'down_right': pygame.transform.rotate(wall_corner, 270),
            }
        }

        self.out_of_bounds_texture = grass
        self.wall_textures = wall_textures


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        # If the application is bundled by PyInstaller
        base_path = sys._MEIPASS
    else:
        # If the application is running in a development environment
        # Adjust the following line to correctly point to your project root
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    return os.path.join(base_path, relative_path)
