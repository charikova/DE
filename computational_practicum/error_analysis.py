import base64

from computational_practicum import euler_method, improved_euler_method, runge_kutta_method, exact_solution
from matplotlib import pyplot as plt
import os
from django.shortcuts import render

from computational_practicum.models import Post


def analysis(request):
    q = Post.objects.all()
    x0 = q[0].x0
    y0 = q[0].y0
    x = q[0].x
    n = q[0].n

    max_error_euler = []
    max_error_improved_euler = []
    max_error_runge_kutta = []
    xx = []

    for i in range(1, int(n) - 1):
        xx.append(i)
        xs_e, ys_e = euler_method.computations(x0, y0, x, i)
        xs_ie, ys_ie = improved_euler_method.computations(x0, y0, x, i)
        xs_rk, ys_rk = runge_kutta_method.computations(x0, y0, x, i)
        xs_es, ys_es = exact_solution.computations(x0, y0, x, i)

        imax_error_euler = []
        imax_error_improved_euler = []
        imax_error_runge_kutta = []

        for j in range(i):
             imax_error_euler.append(abs(ys_es[j] - ys_e[j]))
             imax_error_improved_euler.append(abs(ys_es[j] - ys_ie[j]))
             imax_error_runge_kutta.append(abs(ys_es[j] - ys_rk[j]))

        max_error_euler.append(max(imax_error_euler))
        max_error_improved_euler.append(max(imax_error_improved_euler))
        max_error_runge_kutta.append(max(imax_error_runge_kutta))

    plt.plot(xx, max_error_euler, xx, max_error_improved_euler, xx, max_error_runge_kutta)
    plt.xlabel(r'$n$')
    plt.ylabel(r'$y$')
    plt.grid(True)
    plt.savefig(os.getcwd() + "/computational_practicum/Templates/error_analysis.png")
    plt.show()

    with open(os.getcwd() + "/computational_practicum/Templates/error_analysis.png", 'rb') as img:
        e_a = str(base64.b64encode(img.read()))
    e_a = e_a[1:]
    e_a = e_a.replace('\'', '')

    return render(request, 'computational_practicum/error_analysis.html', {'x0': x0, 'y0': y0, 'x': x, 'n': n,
                                                                         'image_error_analysis': e_a})
