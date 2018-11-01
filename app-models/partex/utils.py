from .apps.users.models import Authenticator

def check_auth(auth_token, user_id):
    res = Authenticator.objects.filter(auth=auth_token, user__id=user_id)
    return res.exists()
