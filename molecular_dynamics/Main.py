#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class System:
    """
    class to simulate the particle constrained by a spring from the
    origin and an intense magnetic field in the z-axis.
    """

    def __init__(self):
        """ initial conditions of the system """
        self.data = np.zeros((1, 4))
        self.data[0, :2] = 10
        self.accel = self.calc_accel()

    def calc_accel(self):
        """ calculate and return acceleration """
        k = 1           # spring constant
        qB = 5          # coefficient for the magnetic field.
        accel = np.zeros((1, 2))
        # implement forces of a spring from the origin and a strong manetic filed
        accel[:, 0] = -k * self.data[:, 0] - qB * self.data[:, 3]
        accel[:, 1] = -k * self.data[:, 1] + qB * self.data[:, 2]
        return accel

    def timestep(self):
        """ update the system for 1 time step """
        _h = 0.001      # time step length = 0.001
        dim = 2         # dimension of the system. 2D
        # velocity verlat solution for the differential equation of motion:
        self.data[:, :dim] += self.data[:, dim:] * _h + 0.5 * self.accel * _h ** 2
        self.data[:, dim:] += self.accel * _h * 0.5
        self.accel = self.calc_accel()
        self.data[:, dim:] += 0.5 * self.accel * _h

    def animate_system(self):
        """ class module to animate the system. """
        def animate(i):
            """ animate function for the simulation """
            for _ in range(20):
                self.timestep()
            line.set_data(x_particles, y_particles)
            ax.set_title(f"step = {i}")

            return line,
        # initialize a plot
        fig, ax = plt.subplots()
        # set proper limits for the plot coordinates
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
        # categorize particle to use in animate()
        x_particles = self.data[:, 0]
        y_particles = self.data[:, 1]

        line, = ax.plot([], [], 'b.', ms=8)     # draw the dot on the plot

        ani = animation.FuncAnimation(fig, animate, interval=20, blit=False,
                save_count=500)
        # live preview if the animation:
        plt.show()
        # save the animation below:
        # ani.save('animation.mp4', writer='imagemagick', fps=20, dpi=200)

def main():
    """ main body """
    system = System()
    system.animate_system()


if __name__ == "__main__":
    main()
