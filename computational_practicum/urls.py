from django.conf.urls import url

from computational_practicum import error_analysis, get_solution, clean
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^solution/', views.solution, name='solution'),
    url(r'^get_solution/', get_solution.get_images, name='get_solution'),
    url(r'^/', views.solution, name='solution'),
    url(r'^error_analysis/', error_analysis.analysis, name='error_analysis'),
    url(r'^get_solution/', get_solution.get_images, name='get_image'),
    url(r'^solution/', clean.clean_db, name='finish')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)