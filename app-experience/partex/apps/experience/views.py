from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

# Create your views here.

def index(request):
    return JsonResponse({
        "ok":True,
        "result":"experience"
    })
