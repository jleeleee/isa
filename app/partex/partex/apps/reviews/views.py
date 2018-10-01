from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Review index")

def create(request):
    return HttpResponse("Review create")
