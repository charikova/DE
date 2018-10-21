from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

from computational_practicum import euler_method
from computational_practicum import improved_euler_method
from computational_practicum import runge_kutta_method


def solution(request):
    parser(request)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
    else:
        form = PostForm()
    return render(request, 'computational_practicum/solution.html', {'form': form})


def parser(request):
    q = Post.objects.all()
    x0 = ([q[0].x0])
    y0 = ([q[0].y0])
    x = ([q[0].x])
    n = ([q[0].n])
    Post.clean(Post)
    euler_method.computations(x0[-1], y0[-1], x[-1], n[-1])
    improved_euler_method.computations(x0[-1], y0[-1], x[-1], n[-1])
    runge_kutta_method.computations(x0[-1], y0[-1], x[-1], n[-1])

    return render(request, 'computational_practicum/get_solution.html', {'x0': x0, 'y0': y0, 'x': x, 'n': n})