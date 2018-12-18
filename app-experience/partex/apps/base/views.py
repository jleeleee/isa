from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .utils import send_data_to_models

import urllib.request
import urllib.parse
import json

from kafka import KafkaProducer

# Create your views here.

def homepage(request):
    try:
        req = urllib.request.Request("http://models:8000/api/v1/listings/recent")
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    except urllib.error.HTTPError as e:
        return JsonResponse({
            "ok": False,
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
            "ok": False,
            "error": str(e.reason),
            "str": str(e)
        })

    try:
        item = listing["result"]["base_item"]

        req = urllib.request.Request("http://models:8000/api/v1/reviews/item/{}".format(item))
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        reviews = json.loads(resp_json)["result"]

    except (urllib.error.HTTPError, KeyError) as e:
        reviews = []

    print(listing)
    if "user_id" in request.POST:
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        producer.send('recommendations', json.dumps({"user_id": request.POST["user_id"], "item_id": _id}).encode('utf-8'))

    return JsonResponse({
        "ok": True,
        "listing": listing["result"],
        "reviews": reviews,
        "recommendations": [listing["result"]]
    })

def all_listings(request):
    # Returns all active listings
    try:
        req = urllib.request.Request("http://models:8000/api/v1/listings/")
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    except urllib.error.HTTPError as e:
        return JsonResponse({
            "ok": False,
            "error": str(e.reason),
            "str": str(e)
        })

    return JsonResponse({
        "ok": True,
        "listings": resp["result"]
    })

@require_http_methods(["POST"])
def create_listing(request):
    rdata = request.POST
    data = {
        "auth":        request.POST.get("auth", None),
        "name":        request.POST.get("name", None),
        "price":       request.POST.get("price", None),
        "seller":      request.POST.get("user_id", None),
        "user_id":     request.POST.get("user_id", None),
        "description": request.POST.get("description", None)
    }

    response = send_data_to_models("listings/create", data)
    if response["ok"]:
        listing = response["result"]
        listing = {
            "name":        listing["name"],
            "description": listing["description"],
            "id":          listing["id"]
        }
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        producer.send('new-listings-topic', json.dumps(listing).encode('utf-8'))

    return JsonResponse(response)

def register(request):
    data = {
        "first_name": request.POST.get("first_name", None),
        "last_name":  request.POST.get("last_name", None),
        "username":   request.POST.get("username", None),
        "password":   request.POST.get("password", None),
        "email":      request.POST.get("email", None)
    }
    return JsonResponse(send_data_to_models("users/create", data))

def login(request):
    data = {
        "username":   request.POST.get("username", None),
        "password":   request.POST.get("password", None)
    }
    return JsonResponse(send_data_to_models("users/login", data))

def logout(request):
    data = {
        "user_id": request.POST.get("user_id", None),
        "auth":    request.POST.get("auth",    None)
    }
    return JsonResponse(send_data_to_models("users/logout", data))
