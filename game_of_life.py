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
                s = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue
                        s += g[(i + di) % nx, (j + dj) % ny]
                n[i, j] = s
        return n

    def step(self) -> None:
        n = self.count_neighbours()
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
    game = GameOfLife("./data/ships.txt")
    game.run(steps=400, pause=0.05)


if __name__ == "__main__":
    main()
