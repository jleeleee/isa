from django.utils.functional import SimpleLazyObject

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.has_auth = bool(request.COOKIES.get("auth"))
        response = self.get_response(request)

        return response
