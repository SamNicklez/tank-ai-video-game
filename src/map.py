import pygame


class Map:
    def __init__(self, WIDTH, HEIGHT, TILE_SIZE):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TILE_SIZE = TILE_SIZE
        self.NUM_TILES_WIDTH = WIDTH // TILE_SIZE
        self.NUM_TILES_HEIGHT = HEIGHT // TILE_SIZE

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
        if 0 <= x < self.NUM_TILES_WIDTH and 0 <= y < self.NUM_TILES_HEIGHT:
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
        self.perimeter()
        self.spawn_walls()

    def perimeter(self):
        for i in range(self.NUM_TILES_WIDTH):
            for j in range(self.NUM_TILES_HEIGHT):
                self.set_tile(i, j, "out_of_bounds")

        for i in range(2, self.NUM_TILES_WIDTH - 2):
            for j in range(1, self.NUM_TILES_HEIGHT - 1):
                if i == 2 or i == self.NUM_TILES_WIDTH - 3:
                    self.set_tile(i, j, "vert")
                elif j == 1 or j == self.NUM_TILES_HEIGHT - 2:
                    self.set_tile(i, j, "hori")
                else:
                    self.set_tile(i, j, "in_bounds")

        self.set_tile(2, 1, "corner,down_right")
        self.set_tile(self.NUM_TILES_WIDTH - 3, 1, "corner,down_left")
        self.set_tile(2, self.NUM_TILES_HEIGHT - 2, "corner,up_right")
        self.set_tile(self.NUM_TILES_WIDTH - 3, self.NUM_TILES_HEIGHT - 2, "corner,up_left")

    def spawn_walls(self):
        for i in range(5, 7):
            self.set_tile(i, 6, "hori")
        for j in range(4, 6):
            self.set_tile(7, j, "vert")
        self.set_tile(7, 6, "corner,up_left")

        for i in range(self.NUM_TILES_WIDTH - 7, self.NUM_TILES_WIDTH - 5):
            self.set_tile(i, self.NUM_TILES_HEIGHT - 7, "hori")
        for j in range(self.NUM_TILES_HEIGHT - 6, self.NUM_TILES_HEIGHT - 4):
            self.set_tile(self.NUM_TILES_WIDTH - 8, j, "vert")
        self.set_tile(self.NUM_TILES_WIDTH - 8, self.NUM_TILES_HEIGHT - 7, "corner,down_right")



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
