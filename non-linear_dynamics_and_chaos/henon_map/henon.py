#!/usr/bin/env python

""" simulate the iterations of henon map """

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


def next_henon(x, y):
    a = 1.4
    b = 0.3
    return y + 1 - a * x ** 2, b * x


def main():
    """ main body """
    x = [0]
    y = [0]

    # for _ in range(10000):
    #     new_x, new_y = next_henon(x[-1], y[-1])
    #     x.append(new_x)
    #     y.append(new_y)

    # plt.plot(x, y, ls='', marker='o', ms=1)
    # plt.show()

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.5, 0.5)

    line, = ax.plot([], [], 'g.', ms=1)


    def animate(i):
        new_x, new_y = next_henon(x[-1], y[-1])
        x.append(new_x)
        y.append(new_y)

        line.set_data(x, y)
        ax.set_title(f"step {i}")
        return line,

    ani = FuncAnimation(fig, animate, interval=20, blit=False, save_count=2000)
    ani.save("henon.mp4", writer='ffmpeg', fps=30, dpi=200)

    # plt.show()


if __name__ == "__main__":
    main()
