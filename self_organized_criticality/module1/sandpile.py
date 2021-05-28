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
        self._slope = np.roll(self.count, -1) - self.count  # slope[i] = h[i+1] - h[i]
        self._slope[-1] = -self.count[-1]   # anomaly on edge
        # for i in range(self.size):
        #     if i == self.size - 1:
        #         self._slope[i] = -self.count[i]
        #     else:
        #         self._slope[i] = self.count[i + 1] - self.count[i]   # slope[i] = count[i+1] - count[i]

    def _relax_slope(self):
        """ relax the slope of the site if slope is greater than z_c """
        self.worked = False      # find if function did a job
        n = 1
        for i in range(self.size):
            if self._slope[i] > self._z_c and i == self.size - 1:  # if steep on the right edge
                self.worked = True   # did a job
                n += 1
                self.count[i] -= 1  # take one grain
            elif self._slope[i] > self._z_c:
                self.worked = True   # did a job
                n += 1
                self.count[i] -= 1  # take one grain
                self.count[i+1] += 1  # add to i+1
            else:
                print("else")
                pass    # don't do shit :)
        print(n)
        return self.worked

    def timestep(self):
        """ evolve the system for 1 time step """
        drop = np.random.randint(low=0, high=self.size-1, size=1)     # drop a random grain of sand
        while(self._relax_slope()):     # relax the whole system completely
            self._update_slope()    # update the slope list
            continue
        if self.count[drop] > self.height - 1:     # if the site is full:
            pass        # do nothing
        else:
            self.count[drop] += 1       # update count
            self._update_slope()        # update the slope of each site


def main():
    """ main body """
    sandpile = Sandpile(20, 20, 1)
    for i in range(100):
        print(f"\r step {i}", end="")
        sandpile.timestep()
        print("\n", sandpile._slope)


if __name__ == "__main__":
    main()
