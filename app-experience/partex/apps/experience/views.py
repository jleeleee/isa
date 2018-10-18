from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

import urllib.request
import urllib.parse
import json

# Create your views here.

def homepage(request):
    context = {}

    try:
        req = urllib.request.Request("http://models:8000/api/v1/")
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    except urllib.error.HTTPError as e:
        return JsonResponse({
            "ok": "False",
            "error": str(e.reason),
            "str": str(e)
        })

    return JsonResponse({
        "ok": True,
        "result":"experience"
    })


def listing(request):
    # Returns the page containing info about the listing
    pass

def all_listings(request):
    # Returns all active listings
    pass

def all_reviews(request):
    # Returns all reviews about a given user or item
    pass
