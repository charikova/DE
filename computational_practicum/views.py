import os
import base64
from django.shortcuts import render
from .models import Post
from .forms import PostForm
from computational_practicum import graph_maker, error_analysis


def solution(request):
    if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save()
    else:
        form = PostForm()
    return render(request, 'computational_practicum/solution.html', {'form': form})


def get_image(request):
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


def clean_db(request):
    Post.objects.all().delete()
