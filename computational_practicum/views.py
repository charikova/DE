import os
import base64
from django.shortcuts import render
from .models import Post
from .forms import PostForm
from computational_practicum import euler_method, graph_maker


def solution(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
    else:
        form = PostForm()
    return render(request, 'computational_practicum/solution.html', {'form': form})


def parser(request):
    q = Post.objects.all()
    x0 = q[0].x0
    y0 = q[0].y0
    x = q[0].x
    n = q[0].n
    Post.objects.all().delete()
    base_image_em = get_image_em(request, x0, y0, x, n)
    return render(request, 'computational_practicum/get_solution.html', {'x0': x0, 'y0': y0, 'x': x, 'n': n,
                                                                         'image_em': base_image_em})


def get_image_em(request, x0, y0, x, n):
    graph_maker.graph(x0, y0, x, n)

    with open(os.getcwd()+"/computational_practicum/Templates/solution.png", 'rb') as img:
        s_em = str(base64.b64encode(img.read()))
    s_em = s_em[1:]
    s_em = s_em.replace('\'','')

    return s_em
