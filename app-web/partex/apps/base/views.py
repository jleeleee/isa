from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . import forms

import urllib.request
import urllib.parse
import json

# Create your views here.

def index(request):
    auth = request.COOKIES.get('auth')

    try:
        req = urllib.request.Request("http://exp:8000/api/v1/home")
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    except urllib.error.HTTPError as e:
        return JsonResponse({
            "ok": "False",
            "error": str(e.reason),
            "str": str(e)
        })

    context = {
        "listings": resp["listings"],
        "is_logged_in": not not auth
    }

    return render(request, "index.html", {})

def login(request):
    auth = request.COOKIES.get('auth')
    if auth:
        return HttpResponseRedirect(reverse("home"))

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            response = forms.send_to_exp(request, form, "login")
            return JsonResponse(response)
    else:
        form = forms.LoginForm()

    return render(request, "login.html", {
        "form": form,
        "is_logged_in": False
    })

def listing(request, _id):
    auth = request.COOKIES.get('auth')

    context = {}

    try:
        req = urllib.request.Request("http://exp:8000/api/v1/listings/{}".format(_id))
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    except urllib.error.HTTPError as e:
        return JsonResponse({
            "ok": False,
            "error": str(e.reason),
            "str": str(e)
        })

    reviews = resp["reviews"]
    average_rating = sum([r["rating"] for r in reviews])/len(reviews)

    context = {
        "listing": resp["listing"],
        "reviews": resp["reviews"],
        "average_rating": average_rating,
        "is_logged_in": not not auth
    }

    return render(request, "listing.html", context)

def listing_index(request):
    auth = request.COOKIES.get('auth')

    context = {}

    try:
        req = urllib.request.Request("http://exp:8000/api/v1/all_listings")
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    except urllib.error.HTTPError as e:
        return JsonResponse({
            "ok": False,
            "error": str(e.reason),
            "str": str(e)
        })

    context = {
        "listings": resp["listings"],
        "is_logged_in": not not auth
    }
    return render(request, "listing_index.html", context)

def listing_create(request):
    auth = request.COOKIES.get('auth')

    # If authenticator cookie wasn't set:
    if not auth:
        return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing"))

    if request.method == 'POST':
        form = forms.ListingCreationForm(request.POST)
        if form.is_valid():
            response = forms.send_to_exp(request, form, "listings/create")
            # return HttpResponseRedirect(reverse("listing", kwargs={"id": repons.id})
            return HttpResponse(str(response))
    else:
        form = forms.ListingCreationForm()

    return render(request, "create_listing.html", {
        "form": form,
        "is_logged_in": True
    })

def about(request):
    return render(request, "about.html", {})
