from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return HttpResponse("<h1>Hello world. Como esta?</h1>")
