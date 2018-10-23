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
    base_image_em = get_image_em(request, x0, y0, x, n)
    base_image_iem = get_image_iem(request, x0, y0, x, n)
    base_image_rkm = get_image_rkm(request, x0, y0, x, n)
    return render(request, 'computational_practicum/get_solution.html', {'x0': x0, 'y0': y0, 'x': x, 'n': n,
                                                                         'image_em': base_image_em,
                                                                         'image_iem': base_image_iem,
                                                                         'image_rkm': base_image_rkm})


def get_image_em(request, x0, y0, x, n):
    euler_method.computations(x0, y0, x, n)
    with open(os.getcwd()+"/computational_practicum/Templates/euler_method_solution.png", 'rb') as img:
        s_em = str(base64.b64encode(img.read()))
    s_em = s_em[1:]
    s_em = s_em.replace('\'','')

    return s_em


def get_image_iem(request, x0, y0, x, n):
    improved_euler_method.computations(x0, y0, x, n)
    with open(os.getcwd() + "/computational_practicum/Templates/improved_euler_method_solution.png", 'rb') as img:
        s_iem = str(base64.b64encode(img.read()))
    s_iem = s_iem[1:]
    s_iem = s_iem.replace('\'', '')

    return s_iem


def get_image_rkm(request, x0, y0, x, n):
    runge_kutta_method.computations(x0, y0, x, n)
    with open(os.getcwd() + "/computational_practicum/Templates/runge_kutta_method_solution.png", 'rb') as img:
        s_rkm = str(base64.b64encode(img.read()))
    s_rkm = s_rkm[1:]
    s_rkm = s_rkm.replace('\'', '')

    return s_rkm
