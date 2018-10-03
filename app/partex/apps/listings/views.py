from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm

from .models import Listing

# Create your views here.

def index(request):
    return JsonResponse({
        "ok": True,
        "result": [
            lst.get_dict() for lst in Listing.objects.all()
        ]
    })

def info(request, id_):
    listing = get_object_or_404(Listing, id=id_)

    return JsonResponse({
        "ok": True,
        "result": Listing.get_dict()
    })

@csrf_exempt
@require_http_methods(["POST"])
def create(request):
    required_fields = ["name", "price"]
    if any(map(lambda k: k not in request.POST, required_fields)):
        return JsonResponse({
            "ok": False,
            "message": "Missing a required field: (one of {})".format(required_fields)
        })

    lst = Listing.objects.create(
        name = request.POST["name"],
        price = request.POST["price"]
        )

    lst.save()

    return JsonResponse({
        "ok": True,
        "result": lst.get_dict()
    })

def delete(request, id_):
    lst = Listing.objects.filter(id=id_)
    if lst.exists():
        lst = lst.first()
        lst.delete()

        return JsonResponse({
            "ok": True,
            "result": lst.get_dict()
        })

    return JsonResponse({
        "ok": False
    })

@csrf_exempt
@require_http_methods(["POST"])
def update(request, id_):
    lst = get_object_or_404(Listing, id=id_)

    for i in request.POST:
        if i in hasattr(lst, i):
            lst[i] = request.POST[i]

    lst.save()

    return JsonResponse({
        "ok": True,
        "result": lst.get_dict()
    })
