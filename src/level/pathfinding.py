import pygame

WIDTH = 1280
HEIGHT = 768
TILE_SIZE = 32
NUM_TILES_WIDTH = WIDTH // TILE_SIZE
NUM_TILES_HEIGHT = HEIGHT // TILE_SIZE


class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Estimated cost from current node to end
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def line_intersects_rect(p0, p1, rect):
    # Points of the rectangle
    rect_points = [rect.topleft, rect.topright, rect.bottomright, rect.bottomleft]

    # Check each edge of the rectangle
    for i in range(len(rect_points)):
        p2, p3 = rect_points[i], rect_points[(i + 1) % 4]
        if line_intersects_line(p0, p1, p2, p3):
            return True

    return False


def line_intersects_line(p0, p1, p2, p3):
    # Calculate parts of the line intersection formula
    s1_x = p1[0] - p0[0]
    s1_y = p1[1] - p0[1]
    s2_x = p3[0] - p2[0]
    s2_y = p3[1] - p2[1]

    denom = (-s2_x * s1_y + s1_x * s2_y)
    if denom == 0:  # Lines are parallel
        return False

    s = (-s1_y * (p0[0] - p2[0]) + s1_x * (p0[1] - p2[1])) / denom
    t = (s2_x * (p0[1] - p2[1]) - s2_y * (p0[0] - p2[0])) / denom

    # If s and t are between 0 and 1, lines intersect
    return 0 <= s <= 1 and 0 <= t <= 1


def find_path(start, end, walls):
    start_node = Node(start[0] // TILE_SIZE, start[1] // TILE_SIZE)
    end_node = Node(end[0] // TILE_SIZE, end[1] // TILE_SIZE)

    open_list = []
    closed_list = []
    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            while current_node:
                tile_center_x = (current_node.x * TILE_SIZE) + (TILE_SIZE // 2)
                tile_center_y = (current_node.y * TILE_SIZE) + (TILE_SIZE // 2)
                path.append((tile_center_x, tile_center_y))
                current_node = current_node.parent
            return path[::-1]

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.x + new_position[0], current_node.y + new_position[1])

            if not is_walkable(node_position, walls):
                continue

            new_node = Node(node_position[0], node_position[1], current_node)

            if new_node in closed_list:
                continue

            new_node.g = current_node.g + 1
            new_node.h = abs(new_node.x - end_node.x) + abs(new_node.y - end_node.y)
            new_node.f = new_node.g + new_node.h

            if new_node not in open_list:
                open_list.append(new_node)

    return []


def simplify_zigzags(path, walls):
    simplified_path = [path[0]]
    i = 1

    while i < len(path) - 1:
        current = simplified_path[-1]
        next = path[i]
        after_next = path[i + 1]

        # Check if there is a zigzag pattern
        if is_zigzag(current, next, after_next):
            # Check if we can go directly to after_next without hitting walls
            if not line_intersects_any_wall(current, after_next, walls):
                # If so, skip the next point
                simplified_path.append(after_next)
                i += 2  # Skip the next point and the after_next point
            else:
                # If not, just follow the path normally
                simplified_path.append(next)
                i += 1
        else:
            # No zigzag, follow the path
            simplified_path.append(next)
            i += 1

    # Add the last point if it wasn't added
    if simplified_path[-1] != path[-1]:
        simplified_path.append(path[-1])

    return simplified_path


def is_zigzag(p1, p2, p3):
    # A zigzag is when the direction to p2 and then to p3 is perpendicular
    direction1 = (p2[0] - p1[0], p2[1] - p1[1])
    direction2 = (p3[0] - p2[0], p3[1] - p2[1])
    return direction1[0] * direction2[0] + direction1[1] * direction2[1] == 0


# Use the same line_intersects_any_wall function from before
def line_intersects_any_wall(p0, p1, walls):
    for wall in walls:
        if line_intersects_rect(p0, p1, wall):
            return True
    return False


def line_of_sight(p0, p1, walls):
    line = pygame.draw.line(pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA), (0, 0, 0), p0, p1)
    for wall in walls:
        if line.colliderect(wall):
            return False
    return True


def is_walkable(node_position, walls):
    # Check if the node is within map bounds
    if (node_position[0] < 0 or node_position[1] < 0 or
            node_position[0] >= NUM_TILES_WIDTH or
            node_position[1] >= NUM_TILES_HEIGHT):
        return False

    # Create a rect for the node
    node_rect = pygame.Rect(node_position[0] * TILE_SIZE, node_position[1] * TILE_SIZE,
                            TILE_SIZE, TILE_SIZE)

    # Check if the node rect intersects with any wall rect
    for wall in walls:
        if node_rect.colliderect(wall):
            return False

    return True
