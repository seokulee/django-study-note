from django.urls import path
from . import views

urlpatterns = [
    # /django_app --> PROJECT urls.py
    path('', views.index, name='index'),
    path('simple', views.simple_view, name='simple'),
]