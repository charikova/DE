from cmath import sin, cos
import os
from math import *
from matplotlib import pyplot as plt


def exact_solution(x0, y0, x, n):
    ys_exact = []
    xs_exact = []

    n = int(n)
    h = (x - x0) / n

    xs_exact.append(x0)
    ys_exact.append(y0)

    c = y0/(sin(x0) - sin(x0)*cos(x0))

    for i in range(n - 1):
        x = xs_exact[-1]
        y = c * sin(x) - sin(x) * cos(x)
        x += h
        xs_exact.append(x)
        ys_exact.append(y)


def error_analyzer_euler(xs, ys, xs_exact, ys_exact, n):
    xs_error = []
    ys_error = []
    for i in range(n - 1):
        xs_error.append(xs_exact[i] - xs[i])
        ys_error.append(ys_exact[i] - ys[i])

    graph_plot_euler(xs_error, ys_error)


def error_analyzer_improved_euler(xs, ys, xs_exact, ys_exact, n):
    xs_error = []
    ys_error = []
    for i in range(n - 1):
        xs_error.append(xs_exact[i] - xs[i])
        ys_error.append(ys_exact[i] - ys[i])

    graph_plot_improved_euler(xs_error, ys_error)


def error_analyzer_runge_kutta(xs, ys, xs_exact, ys_exact, n):
    xs_error = []
    ys_error = []
    for i in range(n - 1):
        xs_error.append(xs_exact[i] - xs[i])
        ys_error.append(ys_exact[i] - ys[i])

    graph_plot_runge_kutta(xs_error, ys_error)


def graph_plot_euler(xs, ys):
    plt.plot(xs, ys, '.r-')
    plt.xlabel('Value of x')
    plt.ylabel('Value of y')
    plt.title("Error Analysis")
    plt.savefig(os.getcwd()+"/computational_practicum/Templates/error_euler.png")
    plt.show()


def graph_plot_improved_euler(xs, ys):
    plt.plot(xs, ys, '.r-')
    plt.xlabel('Value of x')
    plt.ylabel('Value of y')
    plt.title("Error Analysis")
    plt.savefig(os.getcwd()+"/computational_practicum/Templates/error_improved_euler.png")
    plt.show()


def graph_plot_runge_kutta(xs, ys):
    plt.plot(xs, ys, '.r-')
    plt.xlabel('Value of x')
    plt.ylabel('Value of y')
    plt.title("Error Analysis")
    plt.savefig(os.getcwd()+"/computational_practicum/Templates/error_runge_kutta.png")
    plt.show()
