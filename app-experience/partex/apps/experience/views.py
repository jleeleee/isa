from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

import urllib.request
import urllib.parse
import json

# Create your views here.

def homepage(request):
    try:
        req = urllib.request.Request("http://models:8000/api/v1/listings/recent")
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
        "listings": resp["result"]
    })

def listing(request, _id):
    # Returns the page containing info about the listing
    try:
        req = urllib.request.Request("http://models:8000/api/v1/listings/{}".format(_id))
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        listing = json.loads(resp_json)

    except urllib.error.HTTPError as e:
        return JsonResponse({
            "ok": "False",
            "error": str(e.reason),
            "str": str(e)
        })

    try:
        item = listing["result"]["base_item"]

        req = urllib.request.Request("http://models:8000/api/v1/reviews/item/{}".format(item))
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        reviews = json.loads(resp_json)["result"]

    except urllib.error.HTTPError as e:
        reviews = []

    return JsonResponse({
        "ok": True,
        "listing": listing["result"],
        "reviews": reviews
    })

def all_listings(request):
    # Returns all active listings
    try:
        req = urllib.request.Request("http://models:8000/api/v1/listings/")
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
        "listings": resp["result"]
    })
