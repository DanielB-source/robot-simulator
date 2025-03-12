from table import Table

MOVEMENTS = {
    "NORTH": (0, 1),
    "SOUTH": (0, -1),
    "EAST": (1, 0),
    "WEST": (-1, 0),
}

RIGHT_TURN = {"NORTH": "EAST", "EAST": "SOUTH", "SOUTH": "WEST", "WEST": "NORTH"}
LEFT_TURN = {"NORTH": "WEST", "WEST": "SOUTH", "SOUTH": "EAST", "EAST": "NORTH"}


class Robot:
    def __init__(self, table=None):
        self.x = None
        self.y = None
        self.direction = None
        self.table = table

    def place(self, x, y, direction):
        if self.table.is_valid_placement(x, y, direction):
            self.x = x
            self.y = y
            self.direction = direction

    def move(self):
        step_x, step_y = MOVEMENTS[self.direction]
        tmp_x = self.x + step_x
        tmp_y = self.y + step_y
        if self.table.is_in_bound(tmp_x, tmp_y):
            self.x = tmp_x
            self.y = tmp_y

    def right(self):
        self.direction = RIGHT_TURN[self.direction]

    def left(self):
        self.direction = LEFT_TURN[self.direction]

    def report(self):
        return f"{self.x},{self.y},{self.direction}"


if __name__ == "__main__":
    t = Table()
    r = Robot(t)
    r.place(10, 20, "SOUTH")
    print(r.report())
    r.place(1, 2, "SOUTH")
    print(r.report())
