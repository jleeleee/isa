from django.http import HttpResponse

import urllib.request
import urllib.parse
import json

def send_to_exp(request, data, path):
    url = "http://exp:8000/api/v1/{}".format(path)

    post_data = data
    post_data["user_id"] = request.COOKIES.get('user_id')
    post_data["auth"] = request.COOKIES.get('auth')

    try:
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req, data=urllib.parse.urlencode(post_data).encode())
        resp_json = res.read().decode('utf-8')
        resp = json.loads(resp_json)
        return resp
    except urllib.error.HTTPError as e:
        return {
            "ok": False,
            "response": str(e.reason)
        }
