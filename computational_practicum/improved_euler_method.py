from math import *
from matplotlib import pyplot as plt
from matplotlib.pyplot import savefig


def computations(x0, y0, x, n):
    xs = []
    ys = []

    xs.append(x0)
    ys.append(y0)

    n = int(n)

    h = (x - x0) / n

    for i in range(n):
        x = xs[-1]
        y = ys[-1]
        y_current = h * ((sin(x) * sin(x)) + (y * (cos(x)/sin(x)))) + y
        x_current = x + h
        ys.append(y_current)
        xs.append(x_current)

    plot(xs, ys)


def plot(xs, ys):
    plt.plot(xs, ys, 'o')
    plt.xlabel('Value of x')
    plt.ylabel('Value of y')
    plt.title("Approximate solution with Improved Euler's Method")
    savefig('improved_euler_method_solution.png')