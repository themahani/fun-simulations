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
        self._slope = self.count - np.roll(self.count, -1) # slope[i] = count[i] - count[i-1]


    def _relax_slope(self):
        """ relax the slope of the site if slope is greater than z_c """
        mask = self._slope > self._z_c  # find places that need relaxation
        print(mask)
        # now relax the slopes ~~~~~~~~~~~~~~~~~~~~~~ BUG! ~~~~~~~~~~~~~~~
        self.count[mask] -= 1       # take from steeps site
        self.canvas[self.count[mask], mask] = 0     # update canvas

        self.count[np.roll(mask, -1)] += 1  # add to left of steep site
        self.canvas[self.count[np.roll(mask, -1)] - 1, np.roll(mask, -1)] = 1    # update canvas


    def timestep(self):
        """ evolve the system for 1 time step """
        drop = np.random.randint(self.size)     # drop a random grain of sand
        if self.count[drop] == self.height - 1:     # if the site is full:
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
    sandpile = Sandpile(20, 20, 2)
    sandpile.animate_system()

if __name__ == "__main__":
    main()
