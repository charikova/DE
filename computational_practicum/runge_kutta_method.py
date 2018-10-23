from math import *
import os
from matplotlib import pyplot as plt
from matplotlib.pyplot import savefig


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
        k2 = function_for_computation(x + (h / 2), y + (k1 / 2))
        k3 = function_for_computation(x + (h / 2), y + (k2 / 2))
        k4 = function_for_computation(x + h, y + k3)
        delta_y = (k1 + (2 * k2) + (2 * k3) + k4) / 6
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
    plt.title("Approximate solution with Runge-Kutta's Method")
    plt.savefig(os.getcwd()+"/computational_practicum/Templates/runge_kutta_method_solution.png")
    plt.show()