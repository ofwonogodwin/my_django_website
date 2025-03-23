from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Praise The Lord")

def greet(request):
    return HttpResponse('Wichiewi neddi Koro')

def greeting(request):
    return HttpResponse('Walwa Winni, Muli Mutya')