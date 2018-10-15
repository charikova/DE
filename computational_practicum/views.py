from django.shortcuts import render


def solution(request):
    return render(request, 'computational_practicum/solution.html', {})