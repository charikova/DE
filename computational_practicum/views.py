from django.shortcuts import render
from .forms import PostForm


def solution(request):
    if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save()
    else:
        form = PostForm()
    return render(request, 'computational_practicum/solution.html', {'form': form})
