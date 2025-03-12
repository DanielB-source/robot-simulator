MOVEMENTS = {
    "NORTH": (0, 1),
    "SOUTH": (0, -1),
    "EAST": (1, 0),
    "WEST": (-1, 0),
}

RIGHT_TURN = {"NORTH": "EAST", "EAST": "SOUTH", "SOUTH": "WEST", "WEST": "NORTH"}
LEFT_TURN = {"NORTH": "WEST", "WEST": "SOUTH", "SOUTH": "EAST", "EAST": "NORTH"}


class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None

    def move(self):
        step_x, step_y = MOVEMENTS[self.direction]
        self.x += step_x
        self.y += step_y

    def place(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def right(self):
        self.direction = RIGHT_TURN[self.direction]

    def left(self):
        self.direction = LEFT_TURN[self.direction]

    def report(self):
        return f"{self.x},{self.y},{self.direction}"


if __name__ == "__main__":
    r = Robot()
    r.place(2, 4, "SOUTH")
    r.left()
    r.left()
    r.right()
    r.move()
    print(r.report())
