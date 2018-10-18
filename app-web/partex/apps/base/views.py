from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json

# Create your views here.

def index(request):
    context = {}

    try:
        req = urllib.request.Request("http://exp:8000/v1/api/listings")
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        resp = json.loads(resp_json)
    except urllib.error.HTTPError as e:
        """
        return JsonResponse({
            "ok": "False",
            "error": str(e.reason),
            "str": str(e)
        })
        context = {
            "ok": resp["ok"],
            "response": resp_json
        }
        """

    return render(request, "index.html", context)
