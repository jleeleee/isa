from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Part index")

def create(request):
    return HttpResponse("Part create")
