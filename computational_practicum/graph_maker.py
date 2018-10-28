import os
from matplotlib import pyplot as plt
from computational_practicum import euler_method, improved_euler_method, runge_kutta_method


def graph(x0, y0, x, n):
    xs_euler, ys_euler = euler_method.computations(x0, y0, x, n)
    xs_improved_euler, ys_improved_euler = improved_euler_method.computations(x0, y0, x, n)
    xs_runge_kutta, ys_runge_kutta = runge_kutta_method.computations(x0, y0, x, n)
    plt.plot(xs_euler, ys_euler, xs_improved_euler, ys_improved_euler, xs_runge_kutta, ys_runge_kutta)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title(r'$Euler_Method,\ Improved_Euler_Method,\ Runge-Kutta_Method$')
    plt.grid(True)
    plt.savefig(os.getcwd() + "/computational_practicum/Templates/solution.png")
    plt.show()

