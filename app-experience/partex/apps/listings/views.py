from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm

def index(request, id_):
    return JsonResponse({
        "ok": True,
        "result": []
    })

def get_user(request, id_):

