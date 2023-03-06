from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pinky(request):
    return HttpResponse('<marquee><h1>pinky is beautifully </h1></marquee>')
