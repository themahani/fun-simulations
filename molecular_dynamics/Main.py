#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class System:

    def __init__(self):
        self.data = np.zeros((1, 4))
        self.data[0, :2] = 10
        self.accel = self.calc_accel()

    def calc_accel(self):
        """ calculate and return acceleration """
        k = 1
        qB = 5
        accel = np.zeros((1, 2))
        accel[:, 0] = -k * self.data[:, 0] - qB * self.data[:, 3]
        accel[:, 1] = -k * self.data[:, 1] + qB * self.data[:, 2]
        return accel

    def timestep(self):
        """ update the system for 1 time step """
        _h = 0.001
        dim = 2
        self.data[:, :dim] += self.data[:, dim:] * _h + 0.5 * self.accel * _h ** 2
        self.data[:, dim:] += self.accel * _h * 0.5
        self.accel = self.calc_accel()
        self.data[:, dim:] += 0.5 * self.accel * _h

    def animate_system(self):
        def animate(i):
            for _ in range(20):
                self.timestep()
            line.set_data(x_particles, y_particles)
            ax.set_title(f"step = {i}")

            return line,

        fig, ax = plt.subplots()

        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)

        x_particles = self.data[:, 0]
        y_particles = self.data[:, 1]

        line, = ax.plot([], [], 'b.', ms=8)

        ani = animation.FuncAnimation(fig, animate, interval=20, blit=False,
                save_count=500)
        plt.show()
        # ani.save('animation.mp4', writer='imagemagick', fps=20, dpi=200)

def main():
    """ main body """
    system = System()
    system.animate_system()


if __name__ == "__main__":
    main()
