from table import Table
from robot import Robot
from input_handler import handle_input_file


def main():
    table = Table()
    robot = Robot(table)
    handle_input_file("input.txt", robot)


if __name__ == "__main__":
    main()
