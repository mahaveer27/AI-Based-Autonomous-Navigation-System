print("AI-Based Autonomous Navigation System Started")
print()

grid = [
    ["S", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", "X", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "G"]
]

print("Simulation Grid:")
for row in grid:
    print(" ".join(row))

print()
print("S = Start")
print("G = Goal")
print("X = Obstacle")