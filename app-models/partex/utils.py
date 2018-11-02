from .apps.users.models import Authenticator

def authentication_required(view):
    def view_auth(request, *args, **kwargs):
        auth_token = request.POST["auth"]
        user_id = request.POST["user_id"]
        authentication_failed = JsonResponse({
            "ok": False,
            "message": "Authentication failed"
        })
        if auth_token == None or user_id == None:
            return authentication_failed
        res = Authenticator.objects.filter(authenticator=auth_token, user__id=user_id)
        if not res.exists() or res.is_expired():
            return authentication_failed
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
