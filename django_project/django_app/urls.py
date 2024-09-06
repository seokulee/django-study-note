from django.urls import path
from . import views

urlpatterns = [
    # /django_app --> PROJECT urls.py
    path('<str:topic>/', views.news_view, name='news'),
    path('<int:num_page>', views.num_page_view, name='num_page'),
    # path('<int:num1>/<int:num2>', views.add_views, name='add_views'),
]