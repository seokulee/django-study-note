from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

NOT_FOUND_MSG = "Not Found Topic"

articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page',
}

# Create your views here.
def news_view(request, topic):
    try:
        return HttpResponse(articles[topic])
    except KeyError:
        return HttpResponseNotFound(NOT_FOUND_MSG)
        # raise Http404("404 GENERIC ERROR") #404.html


# dynamic view
def add_views(request, num1, num2):
    return HttpResponse(f'{num1} + {num2} = {num1 + num2}')