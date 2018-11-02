from .apps.users.models import Authenticator
from django.http import JsonResponse
from django.http import HttpResponseForbidden

def authentication_required(view):
    def view_auth(request, *args, **kwargs):
        auth_token = request.POST.get("auth")
        user_id = request.POST.get("user_id")
        if auth_token == None or user_id == None:
            return HttpResponseForbidden()
        res = Authenticator.objects.filter(authenticator=auth_token, user__id=user_id)
        if not res.exists():
            return HttpResponseForbidden()
        _auth = res.get()
        if _auth.is_expired():
            _auth.delete()
            return HttpResponseForbidden()
        return view(request, *args, **kwargs)
    return view_auth

def required_fields(req_fields):
    def check_fields(view):
        def validate_fields(request, *args, **kwargs):
            if any(map(lambda k: k not in request.POST, req_fields)):
                return JsonResponse({
                    "ok": False,
                    "message": "Missing a required field: (one of {})".format(req_fields)
                })
            return view(request, *args, **kwargs)
        return validate_fields
    return check_fields
