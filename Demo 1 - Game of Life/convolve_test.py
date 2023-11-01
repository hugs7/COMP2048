import numpy as np
from scipy.signal import convolve2d
import conway
import sys

N = 64
#create the game of life object
life = conway.GameOfLife(N)
# life.insertBlinker((0,0))
# life.insertGlider((0, 0))
# life.insertGliderGun((0, 0))

f = open("gosperglidergun.rle", "r")
gliderGunLines = f.read()
print(type(gliderGunLines))
life.insertFromRLE(gliderGunLines)

np.set_printoptions(threshold=sys.maxsize)

arr = life.getStates() #initial state
arr = arr[:10,:15]
print(arr)
# Define the neighborhood mask
neighborhood = np.ones((3, 3))
neighborhood[1, 1] = 0  # Exclude the center element

# Compute the neighbor sum using convolution
neighbor_sum = convolve2d(arr != 0, neighborhood, mode='same', boundary='fill')
print(neighbor_sum)

next_grid = np.zeros_like(arr)
print("Next grid")
print(next_grid)
print()
next_grid[(arr == 1) & ((neighbor_sum < 2) | (neighbor_sum > 3))] = 0
next_grid[(arr == 1) & ((neighbor_sum == 2) | (neighbor_sum == 3))] = 1
next_grid[(arr == 0) & (neighbor_sum == 3)] = 1

# Update the grid with the next state of the cells
arr = next_grid

# Print the result
print(arr)