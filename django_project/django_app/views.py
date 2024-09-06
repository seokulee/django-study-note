from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello! This is a view inside django app")

def simple_view(request):
    return HttpResponse("Simple view")