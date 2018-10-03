from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm

from .models import ItemReview, UserReview 

# UserReview Views
def user_index(request):
    return JsonResponse({
        "ok": True,
        "result": [
            r.get_dict() for r in UserReview.objects.all()
        ]
    })

def user_info(request, id_):
    review = get_object_or_404(UserReview, id=id_)
    return JsonResponse({
        "ok": True,
        "result": review.get_dict()
    })

@csrf_exempt
@require_http_methods(["POST"])
def user_create(request):
    required_fields = ["title", "rating", "body", "author", "subject"]
    if any(map(lambda k: k not in request.POST, required_fields)):
        return JsonResponse({
            "ok": False,
            "message": "Missing a required field: (one of {})".format(required_fields)
        })

    r = UserReview.objects.create(
            title = request.POST["title"],
            rating = request.POST["rating"],
            body = request.POST["body"],
            author = request.POST["author"],
            subject = request.POST["subject"],
        )
    r.save()
    return JsonResponse({
        "ok": True,
        "result": r.get_dict(),
        })

def user_delete(request, id_):
    r = UserReview.objects.filter(id=id_)
    if r.exists():
        review = r.first()
        review.delete()

        return JsonResponse({
            "ok": True,
            "result": review.get_dict()
        })

    return JsonResponse({
        "ok": False
    })

@csrf_exempt
@require_http_methods(["POST"])
def user_update(request, id_):
    r = get_object_or_404(UserReview, id=id_)

    r.title = request.POST["title"],
    r.rating = request.POST["rating"],
    r.body = request.POST["body"],
    r.author = request.POST["author"],
    r.subject = request.POST["subject"],

    r.save()

    return JsonResponse({
        "ok": True,
        "result": u.get_dict()
    })

# ItemReview Views
def item_index(request):
    return JsonResponse({
        "ok": True,
        "result": [
            r.get_dict() for r in ItemReview.objects.all()
        ]
    })

def item_info(request, id_):
    review = get_object_or_404(ItemReview, id=id_)
    return JsonResponse({
        "ok": True,
        "result": review.get_dict()
    })

@csrf_exempt
@require_http_methods(["POST"])
def user_create(request):
    required_fields = ["title", "rating", "body", "author", "subject"]
    if any(map(lambda k: k not in request.POST, required_fields)):
        return JsonResponse({
            "ok": False,
            "message": "Missing a required field: (one of {})".format(required_fields)
        })

    r = ItemReview.objects.create(
            title = request.POST["title"],
            rating = request.POST["rating"],
            body = request.POST["body"],
            author = request.POST["author"],
            subject = request.POST["subject"],
        )
    r.save()
    return JsonResponse({
        "ok": True,
        "result": r.get_dict(),
        })

def item_delete(request, id_):
    r = ItemReview.objects.filter(id=id_)
    if r.exists():
        review = r.first()
        review.delete()

        return JsonResponse({
            "ok": True,
            "result": review.get_dict()
        })

    return JsonResponse({
        "ok": False
    })

@csrf_exempt
@require_http_methods(["POST"])
def item_update(request, id_):
    r = get_object_or_404(ItemReview, id=id_)

    r.title = request.POST["title"],
    r.rating = request.POST["rating"],
    r.body = request.POST["body"],
    r.author = request.POST["author"],
    r.subject = request.POST["subject"],

    r.save()

    return JsonResponse({
        "ok": True,
        "result": u.get_dict()
    })
