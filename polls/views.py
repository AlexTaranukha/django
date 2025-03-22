from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import path
from . import views

def hello(request):
    return HttpResponse("Hello, world, from Python/Django.") 

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


