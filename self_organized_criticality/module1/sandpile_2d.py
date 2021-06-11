#!/usr/bin/env python

from time import time
import numpy as np
from matplotlib import pyplot as plt
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

""" Trying to implement the 2D Sandpile """


class Sandpile:
    """ the sandpile system """
    def __init__(self, size, threshold):
        self.size = size        # size of the system
        self.h_c = threshold    # height threshold criticality
        self.count = np.random.randint(size=(self.size+2, self.size+2), low=0, high=5)  # height matrix
        # self.count = np.zeros(shape=(self.size+2, self.size+2), dtype=int) + 3

    # @staticmethod
    def stabilize(self, i, j):
        """ recursive function to stabilize the sandpile """
        aval_size = 0   # avalanche size
        if i in [0, self.size + 1] or j in [0, self.size + 1]:
            pass # do nothing
        elif self.count[i, j] >= self.h_c: # if site is unstable
            aval_size += 1  # add to counter
            self.count[i, j] -= 4 # drop 4 grains to in either direction
            # drop grains on 4 sides
            self.count[i, j+1] += 1
            self.count[i, j-1] += 1
            self.count[i+1, j] += 1
            self.count[i-1, j] += 1
            aval_size += self.stabilize(i-1, j) # check the site before
            aval_size += self.stabilize(i+1, j) # check the site before
            aval_size += self.stabilize(i, j-1) # check the site before
            aval_size += self.stabilize(i, j+1) # check the site before
        return aval_size    # return avalanche size


    def timestep(self):
        """ evolve the system one timestep """
        drop_pos = np.random.randint(size=2, low=1, high=self.size+1) # pick random site
        self.count[drop_pos[0], drop_pos[1]] += 1       # drop the grain
        aval = 0    # store avalanche size
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                aval += self.stabilize(i, j)        # recursively stabilize the sandpile
        return aval


def main():
    """ main body """
    sandpile1 = Sandpile(50, 4)
    sandpile2 = Sandpile(100, 4)
    sandpile3 = Sandpile(200, 4)
    start = time()
    num = 100000
    avals1 = np.zeros(num)
    avals2 = np.zeros(num)
    avals3 = np.zeros(num)
    for i in range(num):
        print(f"\rstep {i} / {num}", end="")  # print progress
        avals1[i] = sandpile1.timestep() # evolve 1 timestep
        avals2[i] = sandpile2.timestep() # evolve 1 timestep
        avals3[i] = sandpile3.timestep() # evolve 1 timestep

    print(f"\n runtime = {time() - start}") # print runtime

    vals, _ = np.histogram(np.log10(avals1[avals1 != 0]), bins=40)
    plt.plot(np.linspace(1, len(vals), len(vals)), vals, '.', label="size = 50")

    vals, _ = np.histogram(np.log10(avals2[avals2 != 0]), bins=40)
    plt.plot(np.linspace(1, len(vals), len(vals)), vals, '.', label="size = 100")

    vals, _ = np.histogram(np.log10(avals3[avals3 != 0]), bins=40)
    plt.plot(np.linspace(1, len(vals), len(vals)), vals, '.', label="size = 200")
    # plt.hist(np.log10(avals1[avals1 != 0]), bins=100)
    plt.xscale('log')
    plt.legend()
    plt.show()
    plt.savefig(f"plot{num}.jpg", dpi=300)


if __name__ == '__main__':
    main()
