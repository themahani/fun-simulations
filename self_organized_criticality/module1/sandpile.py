#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Sandpile(object):
    """ the 1 dimensional sandpile system """
    def __init__(self, size, height, slope_threshold):
        self.size = size
        self.height = height
        self.count = np.zeros(self.size, dtype=int)    # count for the level of sand in each site
        self._slope = np.zeros(self.size, dtype=int)    # relative slope of each site
        self._z_c = slope_threshold         # slope threshold

    def _update_slope(self):
        """ update the slope for each site """
        self._slope = self.count - np.roll(self.count, -1)   # slope[i] = h[i] - h[i+1]
        self._slope[-1] = self.count[-1]   # anomaly on edge

    def _relax_slope(self):
        """ relax the slope of the site if slope is greater than z_c """
        worked = False      # find if function did a job

        for i in range(self.size):
            if self._slope[i] > self._z_c and i == self.size - 1:  # if steep on the right edge
                self.count[i] -= 1  # take one grain
                worked = True   # did a job
            elif self._slope[i] > self._z_c:
                self.count[i] -= 1  # take one grain
                self.count[i+1] += 1  # add to i+1
                worked = True   # did a job
            else:
                pass    # don't do shit :)
        return worked

    def timestep(self):
        """ evolve the system for 1 time step """
        while self._relax_slope():
            self._update_slope()

        drop = np.random.randint(low=0, high=self.size, size=1)     # drop a random grain of sand
        if self.count[drop] > self.height - 1:     # if the site is full:
            pass        # do nothing
        else:
            self.count[drop] += 1       # update count
            self._update_slope()        # update the slope of each site
            self._relax_slope()


def main():
    """ main body """
    # initialize a sandpile with size 50 and height 400 and z_c = 2
    sandpile = Sandpile(50, 400, 2)
    num = 10000     # number of repetitions
    slopes = np.zeros(num)      # array to store mean of slopes
    for i in range(num):        # repeat
        print(f"\r step {i}", end="")   # log progress
        sandpile.timestep()     # drop one grain of sand and stabilize
        slopes[i] = np.mean(sandpile._slope)    # take mean of slope
    print()     # go to next line

    # graphics
    plt.plot(np.linspace(1, num, num), slopes, label=r"$z_c = 2$")
    plt.grid()
    plt.legend()
    plt.title(f"width of sandpile = {sandpile.size}")
    plt.ylabel(r"$<z>$")
    plt.xlabel("time")
    plt.show()
    print(slopes)
    print(sandpile.count)


if __name__ == "__main__":
    main()
