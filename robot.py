MOVEMENTS = {
    "NORTH": (0, 1),
    "SOUTH": (0, -1),
    "EAST": (1, 0),
    "WEST": (-1, 0),
}


class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None

    def move(self):
        step_x, step_y = MOVEMENTS[self.direction]
        self.x += step_x
        self.y += step_y


if __name__ == "__main__":
    r = Robot()
    r.x = 1
    r.y = 2
    r.direction = "NORTH"
    r.move()
    print(r.x, r.y)
