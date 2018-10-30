from cmath import sin, cos


def computations(x0, y0, x, n):
    ys_exact = []
    xs_exact = []

    n = int(n)
    h = (x - x0) / n

    xs_exact.append(x0)
    ys_exact.append(y0)

    c = y0/(sin(x0)) + cos(x0)

    for i in range(n - 1):
        x = xs_exact[-1]
        y = c * sin(x) - (sin(x) * cos(x))
        x += h
        xs_exact.append(x)
        ys_exact.append(y)

    return xs_exact, ys_exact
