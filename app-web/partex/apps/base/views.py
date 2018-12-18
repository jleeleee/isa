from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . import forms
from .utils import send_to_exp

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

    if not resp["ok"]:
        return HttpResponse(status=404)

    context = {
        "listings": resp["listings"]
    }

    return render(request, "index.html", context)

def register(request):
    auth = request.COOKIES.get('auth')
    if auth:
        return HttpResponseRedirect(reverse("homepage"))

    error = ""
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            response = send_to_exp(request, form.cleaned_data, "register")
            if response["ok"]:
                next = request.GET.get("next", reverse("homepage"))

                http_resp = HttpResponseRedirect(next)
                http_resp.set_cookie("auth", response["auth"])
                http_resp.set_cookie("user_id", response["user_id"])

                return http_resp
            elif "response" in response and response['response'] == 'Forbidden':
                return HttpResponseRedirect(reverse("logout"))
            else:
                if "message" in response:
                    error = response["message"]
    else:
        form = forms.RegisterForm()

    return render(request, "register.html", {
        "form": form,
        "error": error
    })

def login(request):
    auth = request.COOKIES.get('auth')
    if auth:
        return HttpResponseRedirect(reverse("homepage"))

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            response = send_to_exp(request, form.cleaned_data, "login")
            if response["ok"]:
                next = request.GET.get("next", reverse("homepage"))

                http_resp = HttpResponseRedirect(next)
                http_resp.set_cookie("auth", response["auth"])
                http_resp.set_cookie("user_id", response["user_id"])

                return http_resp
    else:
        form = forms.LoginForm()

    return render(request, "login.html", {
        "form": form
    })

def logout(request):
    auth = request.COOKIES.get('auth')
    if not auth:
        return HttpResponseRedirect(reverse("homepage"))

    resp = HttpResponseRedirect(reverse("homepage"))
    resp.set_cookie("auth", "")
    resp.set_cookie("user_id", "")

    send_to_exp(request, {}, "logout")

    return resp

def listing(request, _id):
    resp = send_to_exp(request, {}, "listings/{}".format(_id))

    if not resp["ok"]:
        return HttpResponse(status=404)

    reviews = resp["reviews"]
    if len(reviews) == 0:
        average_rating = None
    else:
        average_rating = sum([r["rating"] for r in reviews])/len(reviews)

    context = {
        "listing": resp["listing"],
        "reviews": resp["reviews"],
        "average_rating": average_rating,
        "recommendations": resp["recommendations"]
    }

    return render(request, "listing.html", context)

def listing_index(request):
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

    if not resp["ok"]:
        return HttpResponse(status=404)

    context = {
        "listings": resp["listings"]
    }
    return render(request, "listing_index.html", context)

def listing_search(request):

    search_error = False

    q = request.GET.get('q')
    if q is not None:
        resp = send_to_exp(request, { 'q': q }, "listings/search")
        if not resp["ok"]:
            search_error = True
        else:
            context = resp["response"]
            context["got_results"] = True
            return render(request, "search.html", context)

    return render(request, "search.html", {
        "q": q,
        "type": "listing",
        "search_error": search_error
    })

def listing_create(request):
    auth = request.COOKIES.get('auth')

    # If authenticator cookie wasn't set:
    if not auth:
        return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_listing"))

    if request.method == 'POST':
        form = forms.ListingCreationForm(request.POST)
        if form.is_valid():
            response = send_to_exp(request, form.cleaned_data, "listings/create")
            if response["ok"]:
                return HttpResponseRedirect(reverse("listing", kwargs={"_id": response["result"]["id"]}))
            elif "response" in response and response['response'] == 'Forbidden':
                return HttpResponseRedirect(reverse("logout"))
    else:
        form = forms.ListingCreationForm()

    return render(request, "create_listing.html", {
        "form": form
    })

def about(request):
    return render(request, "about.html", {})
