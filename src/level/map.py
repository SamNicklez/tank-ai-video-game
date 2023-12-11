import pygame
import os


class Map:
    def __init__(self, game, number):
        self.game = game
        self.number = number

        background_image_path = os.path.join(game.assets_dir, 'background_images', 'Partial Floor.png')
        self.background_image = pygame.image.load(background_image_path).convert()
        self.background_image = pygame.transform.scale(self.background_image, (game.WIDTH, game.HEIGHT))

        self.background = pygame.Surface((self.game.WIDTH, self.game.HEIGHT))

        self.tiles = [[None for _ in range(self.game.WIDTH // self.game.TILE_SIZE)] for _ in range(self.game.HEIGHT // self.game.TILE_SIZE)]
        self.wall_positions = []

        self.out_of_bounds_texture = None
        self.in_bounds_texture = None
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
            elif main_type[0] == 'in_bounds':
                #self.background.blit(self.in_bounds_texture, (x * self.game.TILE_SIZE, y * self.game.TILE_SIZE))
                pass
            else:
                self.wall_positions.append(
                    pygame.Rect(x * self.game.TILE_SIZE, y * self.game.TILE_SIZE, self.game.TILE_SIZE, self.game.TILE_SIZE))
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
                self.set_tile(i, j, "out_of_bounds")

        for i in range(2, self.game.NUM_TILES_WIDTH - 2):
            for j in range(1, self.game.NUM_TILES_HEIGHT - 1):
                if i == 2 or i == self.game.NUM_TILES_WIDTH - 3:
                    self.set_tile(i, j, "vert")
                elif j == 1 or j == self.game.NUM_TILES_HEIGHT - 2:
                    self.set_tile(i, j, "hori")
                else:
                    # self.set_tile(i, j, "in_bounds")
                    pass

        self.set_tile(2, 1, "corner,down_right")
        self.set_tile(self.game.NUM_TILES_WIDTH - 3, 1, "corner,down_left")
        self.set_tile(2, self.game.NUM_TILES_HEIGHT - 2, "corner,up_right")
        self.set_tile(self.game.NUM_TILES_WIDTH - 3, self.game.NUM_TILES_HEIGHT - 2, "corner,up_left")

    def map_wall_1(self):
        for i in range(6, 8):
            self.set_tile(i, 7, "hori")
        for j in range(5, 7):
            self.set_tile(8, j, "vert")
        self.set_tile(8, 7, "corner,up_left")

        for i in range(self.game.NUM_TILES_WIDTH - 8, self.game.NUM_TILES_WIDTH - 6):
            self.set_tile(i, self.game.NUM_TILES_HEIGHT - 8, "hori")
        for j in range(self.game.NUM_TILES_HEIGHT - 7, self.game.NUM_TILES_HEIGHT - 5):
            self.set_tile(self.game.NUM_TILES_WIDTH - 9, j, "vert")
        self.set_tile(self.game.NUM_TILES_WIDTH - 9, self.game.NUM_TILES_HEIGHT - 8, "corner,down_right")

    def map_wall_2(self):
        for i in range(6, 8):
            self.set_tile(i, 7, "hori")
        for j in range(5, 7):
            self.set_tile(8, j, "vert")
        self.set_tile(8, 7, "corner,up_left")

        for i in range(self.game.NUM_TILES_WIDTH - 8, self.game.NUM_TILES_WIDTH - 6):
            self.set_tile(i, self.game.NUM_TILES_HEIGHT - 8, "hori")
        for j in range(self.game.NUM_TILES_HEIGHT - 7, self.game.NUM_TILES_HEIGHT - 5):
            self.set_tile(self.game.NUM_TILES_WIDTH - 9, j, "vert")
        self.set_tile(self.game.NUM_TILES_WIDTH - 9, self.game.NUM_TILES_HEIGHT - 8, "corner,down_right")

        for i in range(6, 8):
            self.set_tile(i, self.game.NUM_TILES_HEIGHT - 8, "hori")
        for j in range(self.game.NUM_TILES_HEIGHT - 7, self.game.NUM_TILES_HEIGHT - 5):
            self.set_tile(8, j, "vert")
        self.set_tile(8, self.game.NUM_TILES_HEIGHT - 8, "corner,down_left")

        for i in range(self.game.NUM_TILES_WIDTH - 8, self.game.NUM_TILES_WIDTH - 6):
            self.set_tile(i, 7, "hori")
        for j in range(5, 7):
            self.set_tile(self.game.NUM_TILES_WIDTH - 9, j, "vert")
        self.set_tile(self.game.NUM_TILES_WIDTH - 9, 7, "corner,up_right")

    def map_wall_3(self):
        for j in range(2, 20):
            self.set_tile(7, j, "vert")

        for j in range(4, 22):
            self.set_tile(10, j, "vert")

        for j in range(2, 20):
            self.set_tile(13, j, "vert")

        for j in range(4, 22):
            self.set_tile(16, j, "vert")

        for j in range(2, 20):
            self.set_tile(19, j, "vert")

        for j in range(4, 22):
            self.set_tile(22, j, "vert")

        for j in range(2, 20):
            self.set_tile(25, j, "vert")

        for j in range(4, 22):
            self.set_tile(28, j, "vert")

        for j in range(2, 20):
            self.set_tile(31, j, "vert")



    def load_textures(self):
        grass = pygame.image.load(f"{self.game.assets_dir}/map/grass.png")
        tile = pygame.image.load(f"{self.game.assets_dir}/map/tile.png")
        wall = pygame.image.load(f"{self.game.assets_dir}/map/wall.png")
        wall_t = pygame.image.load(f"{self.game.assets_dir}/map/wall_t.png")
        wall_corner = pygame.image.load(f"{self.game.assets_dir}/map/wall_corner.png")

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
        self.in_bounds_texture = tile
        self.wall_textures = wall_textures
