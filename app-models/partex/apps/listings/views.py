from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm

from ...utils import authentication_required
from ...utils import required_fields
from .models import Listing
from ..users.models import User

import MySQLdb

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

@require_http_methods(["POST"])
@authentication_required
@required_fields(["name", "price", "seller"])
def create(request):
    lst = Listing.objects.create(
        name = request.POST["name"],
        price = request.POST["price"],
        seller = User.objects.get(id=request.POST["seller"]),
        description = request.POST["description"]
        )

    lst.save()

    return JsonResponse({
        "ok": True,
        "result": lst.get_dict()
    })

@authentication_required
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

@require_http_methods(["POST"])
@authentication_required
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

@require_http_methods(["POST"])
@required_fields(["name"])
def create_abstract(request):
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
    three_most_recent_listings = Listing.objects.filter(status=True).order_by('-date_created')[:3]

    return JsonResponse({
        "ok": True,
        "result": [l.get_dict() for l in three_most_recent_listings]
    })

def recommendations(request, id_):
    db = MySQLdb.connect("db", "www", "$3cureUS", "cs4501")
    cursor = db.cursor()

    cursor.execute("SELECT Recos FROM recommendations WHERE Page={}".format(id_))

    res = cursor.fetchone()
    if res is None or len(res) == 0:
        return JsonResponse({
            "ok": True,
            "result": []
        })

    else:
        ids = list(map(int, res[0].split(",")))
        listings = Listing.objects.filter(id__in=ids)
        recos = [ l.get_dict() for l in listings ]
        return JsonResponse({
            "ok": True,
            "ids": ids,
            "result": recos
        })
