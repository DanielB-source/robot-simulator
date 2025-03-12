class Table:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height

    def is_in_bound(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height


if __name__ == "__main__":
    t = Table()
    print(t.is_in_bound(2, 3))
    print(t.is_in_bound(22, 51))
