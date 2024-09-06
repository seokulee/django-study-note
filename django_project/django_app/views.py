from django.shortcuts import render
from django.http import HttpResponse

articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page',
}

# Create your views here.
def news_view(request, topic):
    return HttpResponse(articles[topic])

# dynamic view
def add_views(request, num1, num2):
    return HttpResponse(f'{num1} + {num2} = {num1 + num2}')