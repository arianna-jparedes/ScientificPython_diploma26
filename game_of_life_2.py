#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

class GameOfLife():
    def __init__(self, file_path):
        field=np.genfromtxt(file_path).transpose()
        self.grid = field

    def count_neighbours(self):
        g = self.grid
        nx, ny = g.shape
        n = np.zeros_like(g)

        for i in range(nx):
            for j in range(ny):
                n[i, j] = g[(i-1)%nx, (j-1)%nx] + g[(i-1)%nx, j%nx] + g[(i-1)%nx, (j+1)%nx] + g[i%nx, (j-1)%nx] + g[i%nx, (j+1)%nx] + g[(i+1)%nx, (j-1)%nx] + g[(i+1)%nx, j%nx] + g[(i+1)%nx, (j+1)%nx]

        return n

    def slice_count(self):
        g = self.grid
        n = np.zeros_like(g)
        
        # Vertical, Horizontal, Diagonal
        n[1:, :] += g[:-1, :]
        n[:-1, :] += g[1:, :]
        n[:, 1:] += g[:, :-1]
        n[:, :-1] += g[:, 1:]
        n[1:, 1:] += g[:-1, :-1]
        n[1:, :-1] += g[:-1, 1:]
        n[:-1, 1:] += g[1:, :-1]
        n[:-1, :-1] += g[1:, 1:]
    
        # Periodicity Horizontal-Horizontal
        n[:, 0] += g[:, -1]
        n[:, -1] += g[:, 0]

        # Periodicity Vertical-Vertical
        n[0, :] += g[-1, :]
        n[-1, :] += g[0, :]

        # Periodicity Diagonal-Horizontal
        n[1:, 0] += g[:-1, -1]
        n[:-1, 0] += g[1:, -1]
        n[1:, -1] += g[:-1, 0]
        n[:-1, -1] += g[1:, 0]

        # Periodicity Diagonal-Vertical
        n[0, 1:] += g[-1, :-1]
        n[0, :-1] += g[-1, 1:]
        n[-1, 1:] += g[0, :-1]
        n[-1, :-1] += g[0, 1:]

        return n

    def roll_count(self):
    g = self.grid

    n = (
        np.roll(g,  1, axis=0) + np.roll(g, -1, axis=0) + np.roll(g,  1, axis=1) + np.roll(g, -1, axis=1) + np.roll(np.roll(g,  1, axis=0),  1, axis=1) + np.roll(np.roll(g,  1, axis=0), -1, axis=1) + np.roll(np.roll(g, -1, axis=0),  1, axis=1) + np.roll(np.roll(g, -1, axis=0), -1, axis=1) 
    )

    return n

    def step(self) -> None:
        n = self.slice_count()
        alive = self.grid == 1

        # Rules:
        survive = alive & ((n == 2) | (n == 3))
        born = (~alive) & (n == 3)

        self.grid[:] = 0
        self.grid[survive | born] = 1

    def run(self, steps, pause):
        plt.figure()
        img = plt.imshow(self.grid, interpolation="nearest")
        plt.axis("off")

        for i in range(steps):
            self.step()
            img.set_data(self.grid)
            plt.pause(pause)

        plt.show()


def main():
    game = GameOfLife("./data/gun.txt")
    game.run(steps=400, pause=0.05)


if __name__ == "__main__":
    main()

