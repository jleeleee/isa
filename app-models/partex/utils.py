from .apps.users.models import Authenticator

def check_auth(auth_dict):
    res = Authenticator.objects.filter(authenticator=auth_dict.auth, user__id=auth_dict.user_id)
    return res.exists() and not Authenticator.is_expired()

def check_fields(request, required_fields):
    if any(map(lambda k: k not in request.POST, required_fields)):
        raise ValueError(JsonResponse({
            "ok": False,
            "message": "Missing a required field: (one of {})".format(required_fields)
        }))
    return True
