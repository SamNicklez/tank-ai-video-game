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

