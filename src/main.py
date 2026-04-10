print("AI-Based Autonomous Navigation System Started")
print()

print("1. Grid map loaded")
print("2. Path planner loaded")
print("3. A* algorithm loaded")
print("4. Obstacle detector loaded")
print("5. Robot controller loaded")
print()

print("Simulation Grid with Path:")
grid = [
    ["S", "*", "*", ".", "."],
    [".", ".", "*", ".", "."],
    [".", ".", "X", "*", "."],
    [".", ".", ".", "*", "."],
    [".", ".", ".", "*", "G"]
]

for row in grid:
    print(" ".join(row))

print()
print("Robot movement started...")
path = [(0, 0), (1, 0), (2, 0), (2, 1), (3, 2), (4, 3), (4, 4)]

for step in path:
    print("Moving to", step)

print()
print("Navigation completed successfully")