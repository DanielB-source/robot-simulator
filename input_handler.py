def handle_input_file(filename, robot):
    commands = {
        "MOVE": robot.move,
        "LEFT": robot.left,
        "RIGHT": robot.right,
        "REPORT": lambda: robot.report() and print(robot.report()),
    }

    with open(filename, "r") as file:
        for line in file:
            command = line.strip().split()
            if not command:
                continue
            if command[0] == "PLACE":
                x, y, direction = command[1].split(",")
                robot.place(int(x), int(y), direction)
                continue
            action = commands.get(command[0])
            if action:
                action()
            else:
                print(f"Invalid command: {command}")
