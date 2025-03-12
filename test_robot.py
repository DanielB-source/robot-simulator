import unittest
from robot import Robot
from table import Table


RIGHT_TURN = {"NORTH": "EAST", "EAST": "SOUTH", "SOUTH": "WEST", "WEST": "NORTH"}
LEFT_TURN = {"NORTH": "WEST", "WEST": "SOUTH", "SOUTH": "EAST", "EAST": "NORTH"}


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.table = Table()
        self.robot = Robot(self.table)

    def test_initial_state(self):
        self.assertFalse(self.robot.is_placed)
        self.assertIsNone(self.robot.x)
        self.assertIsNone(self.robot.y)
        self.assertIsNone(self.robot.direction)

    def test_valid_place(self):
        placements = [(0, 0, "NORTH"), (2, 4, "SOUTH"), (3, 4, "EAST"), (4, 4, "WEST")]
        for x, y, direction in placements:
            self.robot.place(x, y, direction)
            self.assertTrue(self.robot.is_placed)
            self.assertEqual(
                (self.robot.x, self.robot.y, self.robot.direction), (x, y, direction)
            )

    def test_invalid_place(self):
        invalid_placements = [(10, 34, "EAST"), (-1, -4, "NORTH"), (0, 0, "norr")]
        for x, y, direction in invalid_placements:
            self.robot.place(x, y, direction)
            self.assertFalse(self.robot.is_placed)

    def test_valid_move(self):
        moves = [
            (3, 0, "NORTH", (3, 1)),
            (2, 2, "SOUTH", (2, 1)),
            (1, 2, "EAST", (2, 2)),
            (0, 0, "WEST", (0, 0)),
        ]
        for x, y, direction, expected in moves:
            self.robot.place(x, y, direction)
            self.robot.move()
            self.assertEqual((self.robot.x, self.robot.y), expected)

        multiple_moves = [
            (1, 1, "NORTH", 3, (1, 4)),
            (4, 4, "SOUTH", 2, (4, 2)),
            (0, 3, "EAST", 4, (4, 3)),
            (2, 1, "WEST", 2, (0, 1)),
            (4, 4, "NORTH", 3, (4, 4)),
        ]
        for x, y, direction, steps, expected in multiple_moves:
            self.robot.place(x, y, direction)
            for _ in range(steps):
                self.robot.move()
            self.assertEqual((self.robot.x, self.robot.y), expected)

    def test_turn_right(self):
        for direction, expected in RIGHT_TURN.items():
            self.robot.place(2, 2, direction)
            self.robot.right()
            self.assertEqual(self.robot.direction, expected)
        self.robot.place(2, 2, "NORTH")
        self.robot.right()
        self.robot.right()
        self.assertEqual(self.robot.direction, "SOUTH")
        self.robot.right()
        self.robot.right()
        self.assertEqual(self.robot.direction, "NORTH")

    def test_turn_left(self):
        for direction, expected in LEFT_TURN.items():
            self.robot.place(2, 2, direction)
            self.robot.left()
            self.assertEqual(self.robot.direction, expected)

    def test_turn_right_left(self):
        self.robot.place(2, 2, "EAST")
        self.robot.right()
        self.robot.left()
        self.assertEqual(self.robot.direction, "EAST")
        self.robot.place(4, 2, "WEST")
        self.robot.right()
        self.robot.right()
        self.robot.right()
        self.robot.left()
        self.robot.right()
        self.assertEqual(self.robot.direction, "SOUTH")

    def test_report(self):
        self.robot.place(2, 2, "EAST")
        self.assertEqual(self.robot.report(), "2,2,EAST")
        self.robot.place(4, 4, "NORTH")
        self.robot.move()
        self.assertEqual(self.robot.report(), "4,4,NORTH")
        self.robot.place(44, 2, "EAST")
        self.assertEqual(self.robot.report(), "4,4,NORTH")

    def test_prevent_falling_off(self):
        edges = [(0, 4, "NORTH"), (2, 0, "SOUTH"), (4, 2, "EAST"), (0, 1, "WEST")]
        for x, y, direction in edges:
            self.robot.place(x, y, direction)
            self.robot.move()
            self.assertEqual((self.robot.x, self.robot.y), (x, y))

    def test_invalid_initial_placement(self):
        invalid_placements = [
            (0, 5, "NORTH"),
            (-1, 3, "EAST"),
            (5, 2, "WEST"),
            (2, -1, "SOUTH"),
        ]
        for x, y, direction in invalid_placements:
            self.robot.place(x, y, direction)
            self.assertFalse(self.robot.is_placed)

        self.robot.place(4, 4, "NORTH")
        self.assertTrue(self.robot.is_placed)
        self.assertEqual(
            (self.robot.x, self.robot.y, self.robot.direction), (4, 4, "NORTH")
        )

        self.robot.place(10, 4, "EAST")
        self.assertEqual(
            (self.robot.x, self.robot.y, self.robot.direction), (4, 4, "NORTH")
        )


if __name__ == "__main__":
    unittest.main()
