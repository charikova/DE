from django.conf.urls import url

from computational_practicum import error_analysis
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^solution/', views.solution, name='solution'),
    url(r'^get_solution/', views.parser, name='get_solution'),
    url(r'^error_analysis/', error_analysis.exact_solution, name='error_analysis'),
    url(r'^/', views.solution, name='solution'),
    url(r'^get_solution/', views.get_image_em, name='get_image'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)