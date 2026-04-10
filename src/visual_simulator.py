import matplotlib.pyplot as plt
import numpy as np

grid = np.array([
    [1, 2, 2, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 3, 2, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, 2, 4]
])

plt.imshow(grid)
plt.title("Autonomous Navigation Simulation")
plt.show()