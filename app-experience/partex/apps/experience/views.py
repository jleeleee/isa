from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

import urllib.request
import urllib.parse
import json

# Create your views here.

def index(request):
    return JsonResponse({
        "ok":True,
        "result":"experience"
    })

def home(request):
    pass

def listing(request):
    pass

def abstractItem(request):
    pass
