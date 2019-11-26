from django.shortcuts import render
from django.http import HttpResponse
from .city_state_list import *
import json

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def login(request):
    return render(request, 'pages/login.html')

def signup(request):
    return render(request, 'pages/signup.html')

def test(request):
    return render(request, 'pages/test.html')