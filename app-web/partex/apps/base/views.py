from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from . import forms

import urllib.request
import urllib.parse
import json

# Create your views here.

def index(request):
    context = {}

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
        "listings": resp["listings"]
    }

    return render(request, "index.html", context)

def listing(request, _id):
    context = {}

    try:
        req = urllib.request.Request("http://exp:8000/api/v1/listings/{}".format(_id))
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    except urllib.error.HTTPError as e:
        return JsonResponse({
            "ok": "False",
            "error": str(e.reason),
            "str": str(e)
        })

    reviews = resp["reviews"]
    average_rating = sum([r["rating"] for r in reviews])/len(reviews)

    context = {
        "listing": resp["listing"],
        "reviews": resp["reviews"],
        "average_rating": average_rating
    }

    return render(request, "listing.html", context)

def listing_index(request):
    context = {}

    try:
        req = urllib.request.Request("http://exp:8000/api/v1/all_listings")
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    except urllib.error.HTTPError as e:
        return JsonResponse({
            "ok": "False",
            "error": str(e.reason),
            "str": str(e)
        })

    context = {
        "listings": resp["listings"]
    }
    return render(request, "listing_index.html", context)

def listing_create(request):
    auth = request.COOKIES.get('auth')

    # If authenticator cookie wasn't set:
    """
    if not auth:
        return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing"))
    """
    if request.method == 'POST':
        form = forms.ListingCreationForm(request.POST)
        if form.is_valid():
            response = forms.send_to_exp(request, form, "listing/create")
            # return HttpResponseRedirect(reverse("listing", kwargs={"id": repons.id})
            return HttpResponse("Sent")
    else:
        form = forms.ListingCreationForm()

    return render(request, "create_listing.html", {
        "form": form
    })

def about(request):
    return render(request, "about.html", {})
