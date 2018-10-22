import json
import os
import base64

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from PIL import Image


from computational_practicum import euler_method
from computational_practicum import improved_euler_method
from computational_practicum import runge_kutta_method


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
    base_image = get_image(request,x0,y0,x,n)
    print(base_image)
    return render(request, 'computational_practicum/get_solution.html', {'x0': x0, 'y0': y0, 'x': x, 'n': n,'image':base_image})


def get_image(request, x0, y0, x, n):
    image_data_euler = euler_method.computations(x0, y0, x, n)
    with open(os.getcwd()+"/computational_practicum/Templates/euler_method_solution.png", 'rb') as img:
        s = str(base64.b64encode(img.read()))
    s = s[1:]
    s=s.replace('\'','')

    #image_data_improved_euler = improved_euler_method.computations(x0[0], y0[0], x[0], n[0])
    #image_data_runge_kutta = runge_kutta_method.computations(x0[0], y0[0], x[0], n[0])
    return s
