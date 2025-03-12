DIRECTIONS = ["NORTH", "SOUTH", "EAST", "WEST"]


class Table:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height

    def is_in_bound(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def is_valid_direction(self, direction):
        return direction in DIRECTIONS

    def is_valid_placement(self, x, y, direction):
        return self.is_in_bound(x, y) and self.is_valid_direction(direction)
