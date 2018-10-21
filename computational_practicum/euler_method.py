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

        k1 = sin(x) * sin(x) + (y * (cos(x) / sin(x)))
        delta_y = k1
        x_next = x + h
        y_next = y + delta_y

        xs.append(x_next)
        ys.append(y_next)

    plot(xs, ys)


def plot(xs, ys):
    plt.plot(xs, ys, 'o')
    plt.xlabel('Value of x')
    plt.ylabel('Value of y')
    plt.title("Approximate solution with Euler's Method")
    savefig('euler_method_solution.png')
    plt.show()