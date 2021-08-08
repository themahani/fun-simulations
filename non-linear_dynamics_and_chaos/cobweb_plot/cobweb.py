#!/usr/bin/env python

""" Code to draw the cobweb diagram of a recursive fucntion """

import numpy as np
from matplotlib import pyplot as plt


def f(x, r):
    """ the function in question """
    return x * r * (1 - x)


def iterate(func, r, iter_num):
    """ function to generate the cobweb coordinates """
    x = np.random.uniform(0, 1)
    xs = [x]
    ys = [x]

    for i in range(iter_num):
        xs.append(x)
        y = func(x, r)
        ys.append(y)
        x = y
        xs.append(x)
        ys.append(x)

    return xs, ys



def main():
    """ main body """
    x_axis = np.linspace(-1, 1, 1000)
    r = -1
    iteration = 100

    xs, ys = iterate(f, r, iteration)

    fig, ax = plt.subplots(1, 1, figsize=(8, 8))

    ax.plot(x_axis, f(x_axis, r), c='g')
    ax.plot(x_axis, x_axis, c='g')
    ax.plot(xs, ys, c='r')
    ax.set_xlabel(r"$x_{n}$")
    ax.set_ylabel(r"$x_{n+1}$")
    plt.title(f'cobweb plot for r={r}')
    plt.savefig(f'cobweb_r{r}.jpg', dpi=200, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
