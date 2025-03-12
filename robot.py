from table import Table

MOVEMENTS = {
    "NORTH": (0, 1),
    "SOUTH": (0, -1),
    "EAST": (1, 0),
    "WEST": (-1, 0),
}

RIGHT_TURN = {"NORTH": "EAST", "EAST": "SOUTH", "SOUTH": "WEST", "WEST": "NORTH"}
LEFT_TURN = {"NORTH": "WEST", "WEST": "SOUTH", "SOUTH": "EAST", "EAST": "NORTH"}


def requires_placement(method):
    def wrapper(self):
        if not self.is_placed:
            return
        return method(self)

    return wrapper


class Robot:
    def __init__(self, table=None):
        self.x = None
        self.y = None
        self.direction = None
        self.table = table
        self.is_placed = False

    def place(self, x, y, direction):
        if self.table.is_valid_placement(x, y, direction):
            self.x = x
            self.y = y
            self.direction = direction
            self.is_placed = True

    @requires_placement
    def move(self):
        step_x, step_y = MOVEMENTS[self.direction]
        tmp_x = self.x + step_x
        tmp_y = self.y + step_y
        if self.table.is_in_bound(tmp_x, tmp_y):
            self.x = tmp_x
            self.y = tmp_y

    @requires_placement
    def right(self):
        self.direction = RIGHT_TURN[self.direction]

    @requires_placement
    def left(self):
        self.direction = LEFT_TURN[self.direction]

    @requires_placement
    def report(self):
        return f"{self.x},{self.y},{self.direction}"


if __name__ == "__main__":
    t = Table()
    r = Robot(t)
    r.x = 1
    r.y = 2
    r.direction = "NORTH"
    r.move()
    print(r.report())
    t = Table()
    r = Robot(t)
    r.place(1, 2, "NORTH")
    r.move()
    print(r.report())
