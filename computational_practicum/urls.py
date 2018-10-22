from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^solution/', views.solution, name='solution'),
    url(r'^get_solution/', views.parser, name='get_solution'),
    url(r'^/', views.solution, name='solution'),
    url(r'^get_solution/', views.get_image, name='get_image'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)