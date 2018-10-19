from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm

from .models import Listing
from ..users.models import User

# Create your views here.

def index(request):
    return JsonResponse({
        "ok": True,
        "result": [
            lst.get_dict() for lst in Listing.objects.all()
        ]
    })

def info(request, id_):
    lst = get_object_or_404(Listing, id=id_)

    return JsonResponse({
        "ok": True,
        "result": lst.get_dict()
    })

@csrf_exempt
@require_http_methods(["POST"])
def create(request):
    required_fields = ["name", "price", "seller"]
    if any(map(lambda k: k not in request.POST, required_fields)):
        return JsonResponse({
            "ok": False,
            "message": "Missing a required field: (one of {})".format(required_fields)
        })

    lst = Listing.objects.create(
        name = request.POST["name"],
        price = request.POST["price"],
        seller = User.objects.get(id=request.POST["seller"])
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

    lst.name = request.POST.get("name", lst.name)
    lst.price = request.POST.get("price", lst.price)
    lst.status = request.POST.get("status", lst.status)
    lst.description = request.POST.get("description", lst.description)
    lst.seller = request.POST.get("seller", lst.seller)
    lst.base_item = request.POST.get("base_item", lst.base_item)
    lst.date_created = request.POST.get("date_created", lst.date_created)

    lst.save()

    return JsonResponse({
        "ok": True,
        "result": lst.get_dict()
    })

@csrf_exempt
@require_http_methods(["POST"])
def create_abstract(request):
    required_fields = ["name"]
    if any(map(lambda k: k not in request.POST, required_fields)):
        return JsonResponse({
            "ok": False,
            "message": "Missing a required field: (one of {})".format(required_fields)
        })

    item = AbstractItem.objects.create(
        name = request.POST["name"]
        )

    item.save()

    return JsonResponse({
        "ok": True,
        "result": item.get_dict()
    })

def delete_abstract(request, id_):
    item = get_object_or_404(AbstractItem, id=id_);

    if item.exists():
        item = item.first()
        item.delete()

        return JsonResponse({
            "ok": True,
            "result": item.get_dict()
        })

    return JsonResponse({
        "ok": False
    })

def update_abstract(request, id_):
    item = get_object_or_404(AbstractItem, id=id_);

    item.name = request.POST.get("name", item.name)
    item.generic_description = request.POST.get("generic_description", item.generic_description)

    item.save()

    return JsonResponse({
        "ok": True,
        "result": item.get_dict()
    })

def get_three_listings(request):
    three_most_recent_listings = Listing.objects.filter(status=True).order_by('date_created')[:3]

    return JsonResponse({
        "ok": True,
        "result": list(three_most_recent_listings.values("name", "id", "price"))
    })
