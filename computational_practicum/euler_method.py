import os
from math import *
from matplotlib import pyplot as plt


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

    graph_plot(xs, ys)


def function_for_computation(x, y):
    return sin(x) * sin(x) + (y * (cos(x) / sin(x)))


def graph_plot(xs, ys):
    plt.plot(xs, ys, '.r-')
    plt.xlabel('Value of x')
    plt.ylabel('Value of y')
    plt.title("Approximate solution with Euler's Method")
    plt.savefig(os.getcwd()+"/computational_practicum/Templates/euler_method_solution.png")
    plt.show()

