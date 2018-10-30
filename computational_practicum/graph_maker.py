import os
from matplotlib import pyplot as plt
from computational_practicum import euler_method, improved_euler_method, runge_kutta_method, exact_solution


def graph(x0, y0, x, n):
    xs_exact, ys_exact = exact_solution.computations(x0, y0, x, n)
    xs_euler, ys_euler = euler_method.computations(x0, y0, x, n)
    xs_improved_euler, ys_improved_euler = improved_euler_method.computations(x0, y0, x, n)
    xs_runge_kutta, ys_runge_kutta = runge_kutta_method.computations(x0, y0, x, n)

    plt.plot(xs_exact, ys_exact, xs_euler, ys_euler, xs_improved_euler, ys_improved_euler, xs_runge_kutta, ys_runge_kutta)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.grid(True)
    plt.savefig(os.getcwd() + "/computational_practicum/Templates/solution.png")
    plt.show()

    ys_error_euler = []
    for i in range(len(ys_euler) - 1):
        ys_error_euler.append(abs(ys_exact[i] - ys_euler[i]))

    ys_error_improved_euler = []
    for i in range(len(ys_improved_euler) - 1):
        ys_error_improved_euler.append(abs(ys_exact[i] - ys_improved_euler[i]))

    ys_error_runge_kutta = []
    for i in range(len(ys_runge_kutta) - 1):
        i += 1
        ys_error_runge_kutta.append(abs(ys_exact[i] - ys_runge_kutta[i]))

    if len(xs_euler) > len(ys_error_euler):
        xs_euler = xs_euler[:-1]

    if len(xs_euler) < len(ys_error_euler):
        ys_error_euler = ys_error_euler[:-1]

    if len(xs_improved_euler) > len(ys_error_improved_euler):
        xs_improved_euler = xs_improved_euler[:-1]

    if len(xs_improved_euler) < len(ys_error_improved_euler):
        ys_error_improved_euler = ys_error_improved_euler[:-1]

    if len(xs_runge_kutta) > len(ys_error_runge_kutta):
        xs_runge_kutta= xs_runge_kutta[:-1]

    if len(xs_runge_kutta) < len(ys_error_runge_kutta):
        ys_error_runge_kutta = ys_error_runge_kutta[:-1]

    plt.plot(xs_euler, ys_error_euler, xs_improved_euler, ys_error_improved_euler, xs_runge_kutta,
             ys_error_runge_kutta)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.grid(True)
    plt.savefig(os.getcwd() + "/computational_practicum/Templates/solution_error.png")
    plt.show()
