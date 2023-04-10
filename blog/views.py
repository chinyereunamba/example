from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return HttpRequest("<h1>Hello World. How do you do?</h1>")
