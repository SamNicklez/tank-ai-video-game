import pygame


class Map:
    def __init__(self, WIDTH, HEIGHT, TILE_SIZE):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TILE_SIZE = TILE_SIZE

        self.background = pygame.Surface((WIDTH, HEIGHT))

        self.tiles = [[None for _ in range(WIDTH // TILE_SIZE)] for _ in range(HEIGHT // TILE_SIZE)]
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
        if 0 <= x < self.WIDTH // self.TILE_SIZE and 0 <= y < self.HEIGHT // self.TILE_SIZE:
            self.tiles[y][x] = tile_type
            if main_type[0] == 'out_of_bounds':
                self.background.blit(self.out_of_bounds_texture, (x * self.TILE_SIZE, y * self.TILE_SIZE))
            elif main_type[0] == 'in_bounds':
                self.background.blit(self.in_bounds_texture, (x * self.TILE_SIZE, y * self.TILE_SIZE))
            else:
                self.wall_positions.append(
                    pygame.Rect(x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE))
                if main_type[0] == 'vert' or main_type[0] == 'hori':
                    self.background.blit(self.wall_textures[main_type[0]],
                                         (x * self.TILE_SIZE, y * self.TILE_SIZE))
                elif main_type[0] == 't' or main_type[0] == 'corner':
                    self.background.blit(self.wall_textures[main_type[0]][main_type[1]],
                                         (x * self.TILE_SIZE, y * self.TILE_SIZE))

    def initialize_map_tiles(self):
        for i in range(self.WIDTH // self.TILE_SIZE):
            for j in range(self.HEIGHT // self.TILE_SIZE):
                self.set_tile(i, j, "out_of_bounds")

        for i in range(10, (self.WIDTH // self.TILE_SIZE) - 10):
            for j in range(6, (self.HEIGHT // self.TILE_SIZE) - 6):
                if i == 10 or i == (self.WIDTH // self.TILE_SIZE) - 11:
                    self.set_tile(i, j, "vert")
                elif j == 6 or j == (self.HEIGHT // self.TILE_SIZE) - 7:
                    self.set_tile(i, j, "hori")
                else:
                    self.set_tile(i, j, "in_bounds")

        self.set_tile(10, 6, "corner,down_right")
        self.set_tile((self.WIDTH // self.TILE_SIZE) - 11, 6, "corner,down_left")
        self.set_tile(10, (self.HEIGHT // self.TILE_SIZE) - 7, "corner,up_right")
        self.set_tile((self.WIDTH // self.TILE_SIZE) - 11, (self.HEIGHT // self.TILE_SIZE) - 7, "corner,up_left")

    def load_textures(self):
        grass = pygame.image.load('assets/map/grass.png')
        tile = pygame.image.load('assets/map/tile.png')
        wall = pygame.image.load('assets/map/wall.png')
        wall_t = pygame.image.load('assets/map/wall_t.png')
        wall_corner = pygame.image.load('assets/map/wall_corner.png')

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
