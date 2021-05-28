#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Sandpile(object):
    """ the 1 dimensional sandpile system """
    def __init__(self, size, height, slope_threshold):
        self.size = size
        self.height = height
        self.canvas = np.zeros(shape=(self.height, self.size), dtype=int)  # canvas for graphics
        self.count = np.zeros(self.size, dtype=int)    # count for the level of sand in each site
        self._slope = np.zeros(self.size, dtype=int)    # relative slope of each site
        self._z_c = slope_threshold


    def _update_slope(self):
        """ update the slope for each site """
        self._slope = np.roll(self.count, -1) - self.count # slope[i] = count[i+1] - count[i]
        self._slope[-1] = -self.count[-1]      # right side is open


    def _relax_slope(self): # ~~~~~~~~~~~~~~ BUG! ~~~~~~~~~~~~~~~~~
        """ relax the slope of the site if slope is greater than z_c """
        for i in range(self.size):
            if self._slope[i] < self._z_c and i == self.size - 1:  # if steep on the right edge
                self.count[i] -= 1  # take one grain
                self.canvas[self.count[i], i] = 0   # update canvas
            elif self._slope[i] < self._z_c:
                self.count[i] -= 1  # take one grain
                self.canvas[self.count[i], i] = 0   # update canvas
                self.count[i+1] += 1  # add to i+1
                self.canvas[self.canvas[i+1] - 1, i+1] = 1   # update canvas
            else:
                pass    # don't do shit :)


    def timestep(self):
        """ evolve the system for 1 time step """
        drop = np.random.randint(low=0, high=self.size-1, size=1)     # drop a random grain of sand
        if self.count[drop] > self.height - 1:     # if the site is full:
            pass        # do nothing
        else:
            self.canvas[self.count[drop], drop] = 1     # drop the grain
            self.count[drop] += 1       # update count
            self._update_slope()        # update the slope of each site
            self._relax_slope()         # relax the slopes higher than the threshold


    def animate_system(self):
        """ animate the graphics of the canvas """
        def animate(i):
            self.timestep()
            ax.pcolormesh(self.canvas)
            ax.set_title(f"step {i}")

        fig, ax = plt.subplots()

        ani = animation.FuncAnimation(fig, animate, save_count=300, blit=False)
        plt.show()


def main():
    """ main body """
    sandpile = Sandpile(20, 20, -1)
    sandpile.animate_system()

if __name__ == "__main__":
    main()
