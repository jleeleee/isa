from django.shortcuts import render

# Create your views here.

def index(request):
    return JsonResponse({
        "ok":True,
        "result":"experience"
    })
