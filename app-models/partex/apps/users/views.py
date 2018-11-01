from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm

from .models import User

# Create your views here.

def index(request):
    return JsonResponse({
        "ok": True,
        "result": [
            u.get_dict() for u in User.objects.all()
        ]
    })

def info(request, id_):
    user = get_object_or_404(User, id=id_)

    return JsonResponse({
        "ok": True,
        "result": user.get_dict()
    })

@require_http_methods(["POST"])
def create(request):
    required_fields = ["username", "first_name", "last_name", "password"]
    if any(map(lambda k: k not in request.POST, required_fields)):
        return JsonResponse({
            "ok": False,
            "message": "Missing a required field: (one of {})".format(required_fields)
        })

    if User.objects.filter(username=request.POST["username"]).exists():
        return JsonResponse({
            "ok": False,
            "message": "User with specified username already exists"
        })


    u = User.objects.create(
        username = request.POST["username"],
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"]
        )
    u.set_password(request.POST["password"])
    u.save()

    return JsonResponse({
        "ok": True,
        "result": u.get_dict()
    })

def delete(request, id_):
    u = User.objects.filter(id=id_)
    if u.exists():
        user = u.first()
        user.delete()

        return JsonResponse({
            "ok": True,
            "result": user.get_dict()
        })

    return JsonResponse({
        "ok": False
    })

@require_http_methods(["POST"])
def update(request, id_):
    u = get_object_or_404(User, id=id_)

    u.username   = request.POST.get("username", u.username)
    u.first_name = request.POST.get("first_name", u.first_name)
    u.last_name  = request.POST.get("last_name", u.last_name)

    if "password" in request.POST:
        u.set_password(request.POST["password"])

    u.save()

    return JsonResponse({
        "ok": True,
        "result": u.get_dict()
    })
