def detect_obstacle(position):
    obstacles = [(2, 2), (3, 1)]

    if position in obstacles:
        return True
    return False


robot_position = (2, 2)

if detect_obstacle(robot_position):
    print("Obstacle detected at", robot_position)
else:
    print("Path is clear")