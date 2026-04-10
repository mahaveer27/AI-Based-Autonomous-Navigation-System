def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

start = (0, 0)
goal = (4, 4)

print("A* path planning module initialized")
print(f"Heuristic from {start} to {goal}: {heuristic(start, goal)}")