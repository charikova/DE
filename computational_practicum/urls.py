from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^solution/', views.solution, name='solution'),
    url(r'^get_solution/', views.parser, name='get_solution'),
    url(r'^/', views.solution, name='solution'),
]
