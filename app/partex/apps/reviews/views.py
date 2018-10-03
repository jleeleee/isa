from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm

from .models import ItemReview, UserReview
from ..users.models import User
from ..listings.models import AbstractItem

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
    required_fields = ["title", "rating", "body","author", "subject"]
    if any(map(lambda k: k not in request.POST, required_fields)):
        return JsonResponse({
            "ok": False,
            "fuck": str(request.POST),
            "message": "Missing a required field: (one of {})".format(required_fields)
        })

    author = User.objects.filter(id=request.POST["author"])
    if author.exists():
        author = author.first()
    else:
        return JsonResponse({
            "ok": False,
            "message": "Author does not exist"
        })

    subject = User.objects.filter(id=request.POST["subject"])
    if subject.exists():
        subject = subject.first()
    else:
        return JsonResponse({
            "ok": False,
            "message": "Subject does not exist"
        })

    r = UserReview.objects.create(
            title = request.POST["title"],
            rating = request.POST["rating"],
            body = request.POST["body"],
            author = author,
            subject = subject
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

    r.title = request.POST.get("title", r.title)
    r.rating = request.POST.get("rating", r.rating)
    r.body = request.POST.get("body", r.body)

    if "author" in request.POST:
        author = User.objects.filter(id=request.POST["author"])
        if author.exists():
            r.author = author.first()
        else:
            return JsonResponse({
                "ok": False,
                "message": "Author does not exist"
            })

    if "subject" in request.POST:
        subject = User.objects.filter(id=request.POST["subject"])
        if subject.exists():
            r.subject = subject.first()
        else:
            return JsonResponse({
                "ok": False,
                "message": "Subject does not exist"
            })

    r.save()

    return JsonResponse({
        "ok": True,
        "result": r.get_dict()
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
def item_create(request):
    required_fields = ["title", "rating", "body", "author", "subject"]
    if any(map(lambda k: k not in request.POST, required_fields)):
        return JsonResponse({
            "ok": False,
            "message": "Missing a required field: (one of {})".format(required_fields)
        })

    author = User.objects.filter(id=request.POST["author"])
    if author.exists():
        author = author.first()
    else:
        return JsonResponse({
            "ok": False,
            "message": "Author does not exist"
        })

    subject = AbstractItem.objects.filter(id=request.POST["subject"])
    if subject.exists():
        subject = subject.first()
    else:
        return JsonResponse({
            "ok": False,
            "message": "Subject does not exist"
        })

    r = ItemReview.objects.create(
            title = request.POST["title"],
            rating = request.POST["rating"],
            body = request.POST["body"],
            author = author,
            subject = subject
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

    r.title = request.POST.get("title", r.title)
    r.rating = request.POST.get("rating", r.rating)
    r.body = request.POST.get("body", r.body)

    if "author" in request.POST:
        author = User.objects.filter(id=request.POST["author"])
        if author.exists():
            r.author = author.first()
        else:
            return JsonResponse({
                "ok": False,
                "message": "Author does not exist"
            })

    if "subject" in request.POST:
        subject = AbstractItem.objects.filter(id=request.POST["subject"])
        if subject.exists():
            r.subject = subject.first()
        else:
            return JsonResponse({
                "ok": False,
                "message": "Subject does not exist"
            })

    r.save()

    return JsonResponse({
        "ok": True,
        "result": r.get_dict()
    })
