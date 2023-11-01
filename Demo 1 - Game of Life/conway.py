# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
import scipy
# import cupy as np
import rle

class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.int)
        self.neighborhood = np.ones((3,3), np.int) # 8 connected kernel
        self.neighborhood[1,1] = 0 #do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        
    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid
    
    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()

    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''

        if self.fastMode:

            # Set up the padding for the edges of the grid
            # pad_width = ((1, 1), (1, 1))
            # grid_padded = np.pad(self.grid, pad_width, mode='constant', constant_values=0)

            # Compute the neighbor sum
            # neighbor_sum = scipy.signal.convolve2d(self.grid != 0, self.neighborhood, mode='same', boundary='fill')
                                                                        # (fillvalue=0) this is done by default
            neighbor_sum = scipy.signal.convolve(self.grid != 0, self.neighborhood, mode='same', method='fft')
                                # fft method is faster than convolving directly with sums
            # Apply the game of life rules
            next_grid = np.zeros_like(self.grid)
            next_grid[(self.grid == self.aliveValue) & ((neighbor_sum < 2) | (neighbor_sum > 3))] = self.deadValue
            next_grid[(self.grid == self.aliveValue) & ((neighbor_sum == 2) | (neighbor_sum == 3))] = self.aliveValue
            next_grid[(self.grid == self.deadValue) & (neighbor_sum == 3)] = self.aliveValue
        else:
            # Create a copy of the current grid to store the next state of the cells
            next_grid = np.zeros_like(self.grid)

            # Get the size of the grid
            n, m = self.grid.shape
            # print(n,m)

            # Loop over each cell in the grid
            for i in range(n):
                for j in range(m):
                    # print(i, j)
                    # Get the indices of the neighborhood cells
                    i_min = max(i - 1, 0)
                    i_max = min(i + 1 + 1, n)
                    j_min = max(j - 1, 0)
                    j_max = min(j + 1 + 1, m)
                    # print()
                    # print("imin", i_min)
                    # print("imax", i_max)
                    # print("jmin", j_min)
                    # print("jmax", j_max)
                    if i == 0:
                        n_min_i = 1
                    else:
                        n_min_i = 0
                    if j == 0:
                        n_min_j = 1
                    else:
                        n_min_j = 0

                    if i == n - 1:
                        n_max_i = 1+1
                    else:
                        n_max_i = 2+1
                    if j == m - 1:
                        n_max_j = 1+1
                    else:
                        n_max_j = 2+1
                    # print()
                    # print("nimin", n_min_i)
                    # print("nimax", n_max_i)
                    # print("njmin", n_min_j)
                    # print("njmax", n_max_j)

                    # print()
                    # print(self.grid[i_min:i_max, j_min:j_max])
                    # print(self.neighborhood[n_min_i:n_max_i, n_min_j:n_max_j])
                    # Get the number of alive neighbors for the current cell
                    alive_neighbors = np.sum(
                        self.grid[i_min:i_max, j_min:j_max] * self.neighborhood[n_min_i:n_max_i, n_min_j:n_max_j])

                    # Check if the current cell is alive
                    if self.grid[i, j] == self.aliveValue:
                        # Check if the cell dies due to underpopulation or overpopulation
                        if alive_neighbors < 2 or alive_neighbors > 3:
                            next_grid[i, j] = self.deadValue
                        else:
                            next_grid[i, j] = self.aliveValue
                    else:
                        # Check if a dead cell becomes alive due to reproduction
                        if alive_neighbors == 3:
                            next_grid[i, j] = self.aliveValue

        # Update the grid with the next state of the cells
        self.grid = next_grid

    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        
    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue
        
    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0]+1, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+2, index[1]+23] = self.aliveValue
        self.grid[index[0]+2, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+3, index[1]+13] = self.aliveValue
        self.grid[index[0]+3, index[1]+14] = self.aliveValue
        self.grid[index[0]+3, index[1]+21] = self.aliveValue
        self.grid[index[0]+3, index[1]+22] = self.aliveValue
        self.grid[index[0]+3, index[1]+35] = self.aliveValue
        self.grid[index[0]+3, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+4, index[1]+12] = self.aliveValue
        self.grid[index[0]+4, index[1]+16] = self.aliveValue
        self.grid[index[0]+4, index[1]+21] = self.aliveValue
        self.grid[index[0]+4, index[1]+22] = self.aliveValue
        self.grid[index[0]+4, index[1]+35] = self.aliveValue
        self.grid[index[0]+4, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+5, index[1]+1] = self.aliveValue
        self.grid[index[0]+5, index[1]+2] = self.aliveValue
        self.grid[index[0]+5, index[1]+11] = self.aliveValue
        self.grid[index[0]+5, index[1]+17] = self.aliveValue
        self.grid[index[0]+5, index[1]+21] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue
        
        self.grid[index[0]+6, index[1]+1] = self.aliveValue
        self.grid[index[0]+6, index[1]+2] = self.aliveValue
        self.grid[index[0]+6, index[1]+11] = self.aliveValue
        self.grid[index[0]+6, index[1]+15] = self.aliveValue
        self.grid[index[0]+6, index[1]+17] = self.aliveValue
        self.grid[index[0]+6, index[1]+18] = self.aliveValue        # Value that I fixed up. Was 17, 6
        self.grid[index[0]+6, index[1]+23] = self.aliveValue
        self.grid[index[0]+6, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+7, index[1]+11] = self.aliveValue
        self.grid[index[0]+7, index[1]+17] = self.aliveValue
        self.grid[index[0]+7, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+8, index[1]+12] = self.aliveValue
        self.grid[index[0]+8, index[1]+16] = self.aliveValue
        
        self.grid[index[0]+9, index[1]+13] = self.aliveValue
        self.grid[index[0]+9, index[1]+14] = self.aliveValue
        
    def insertFromPlainText(self, txtString, pad=0):
        '''
        Assumes txtString contains the entire pattern as a human readable pattern without comments
        '''
        grid_str = txtString.split("\n")
        print(grid_str)
        for x, row in enumerate(grid_str):
            for y, col in enumerate(row):
                if col == 'O':
                    print("Alive at", x, y)
                    self.grid[x, y] = self.aliveValue
                elif col == '.':
                    print("Dead at", x, y)

        print("Done")

    def insertFromRLE(self, rle_str, pad=0):
        '''
        Given string loaded from RLE file, populate the game grid
        '''
        # print("-" * 20)
        # print(rle_str)
        # print("-" * 20)
        # print(rle_str.split("\n"))
        lines = rle_str.split("\n")
        grid = []
        grid_str = ""
        pad_x, pad_y = 20, 20
        for line in lines:
            if line[0] == '#':
                continue
            elif line[0] == 'x':
                parts = line.split(',')
                x = int(parts[0].split('=')[1])
                y = int(parts[1].split('=')[1])
                print("Grid x,y:", x, y)
                # Add pad_x and pad_y to x and y of grid respectively
                self.grid = np.zeros((x+pad_x,y+pad_y), np.int)
            else:
                # Time for actually reading the grid
                # First need to combine all the remaining rows into one big string
                grid_str += line

        # Processing the RLE formatted grid


        rows = grid_str.split("$")
        # print("Rows", rows)
        # print("-"*50)
        for k, row in enumerate(rows):
            sec = []
            num = 0
            # print("----\nRow", k, " : ", row)
            for j, char in enumerate(row):
                if char.isdigit():
                    num *= 10
                    num += int(char)
                elif char == "b":
                    if num == 0:
                        num = 1
                    sec.append((num, char))
                    num = 0
                elif char == "o":
                    if num == 0:
                        num = 1
                    sec.append((num, char))
                    num = 0
                elif char == "!":
                    print("End of grid")

            grid.append(sec)

            # print(grid[k])

        print(grid)

        # print("-"*10)


        # Finished processing rle file
        # Now for creating the Grid
        print(np.shape(self.grid))
        for i, row in enumerate(grid): # Rows
            # print("Row", i)
            ctr = 0 + pad_x // 2     # like the column selector
            # print(row)
            # print()
            for j, section in enumerate(row):
                cnt, type = section
                if type == "b":     # Dead
                    # print("Start:", ctr, ", Stop", ctr + cnt,
                    # ", Steps:", cnt, "Dead")
                    ctr += cnt
                elif type == "o":
                    # print("Start:", ctr, ", Stop", ctr + cnt,
                    #       ", Steps:", cnt, "Alive")
                    for k in range(ctr, ctr + cnt):
                        # print(k)
                        self.grid[k, i + pad_y // 2] = self.aliveValue
                    ctr += cnt

            # print(self.grid[:,i])

        # print("\n\n\n\n")

        self.grid = self.grid.transpose()