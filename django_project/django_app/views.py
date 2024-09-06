from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

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


# domain.com/django_app/0 ---> domain.com/django_app/sports
def num_page_view(request, num_page):
    topics_list = list(articles.keys()) # ['sports', 'finance', 'politics']
    try:
        topic = topics_list[num_page]
    except IndexError:
        return HttpResponseNotFound(NOT_FOUND_MSG)

    return HttpResponseRedirect(reverse('topic-page', args=[topic]))


# # dynamic view
# def add_views(request, num1, num2):
#     return HttpResponse(f'{num1} + {num2} = {num1 + num2}')
