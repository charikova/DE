from math import *
from computational_practicum import graph_maker


def computations(x0, y0, x, n):
    xs = []
    ys = []

    xs.append(x0)
    ys.append(y0)

    n = int(n)
    h = (x - x0) / n

    for i in range(n - 1):
        x = xs[-1]
        y = ys[-1]

        k1 = function_for_computation(x, y)
        delta_y = k1
        x_next = x + h
        y_next = y + delta_y

        xs.append(x_next)
        ys.append(y_next)
    return xs, ys


def function_for_computation(x, y):
    return sin(x) * sin(x) + (y * (cos(x) / sin(x)))


