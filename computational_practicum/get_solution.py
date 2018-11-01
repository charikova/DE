from computational_practicum import graph_maker, error_analysis
from computational_practicum.models import Post
from django.shortcuts import render
import os
import base64


def get_images(request):
    q = Post.objects.all()
    x0 = q[len(Post.objects.all()) - 1].x0
    y0 = q[len(Post.objects.all()) - 1].y0
    x = q[len(Post.objects.all()) - 1].x
    n = q[len(Post.objects.all()) - 1].n

    graph_maker.graph(x0, y0, x, n)

    with open(os.getcwd() + "/computational_practicum/Templates/solution.png", 'rb') as img:
        s = str(base64.b64encode(img.read()))
    s = s[1:]
    s = s.replace('\'', '')

    with open(os.getcwd() + "/computational_practicum/Templates/solution_error.png", 'rb') as img:
        s_e = str(base64.b64encode(img.read()))
    s_e = s_e[1:]
    s_e = s_e.replace('\'', '')

    error_analysis.analysis(request)

    return render(request, 'computational_practicum/get_solution.html', {'x0': x0, 'y0': y0, 'x': x, 'n': n,
                                                                         'image': s,
                                                                         'image_error': s_e,
                                                                         })