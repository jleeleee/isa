import json
import urllib.error
import urllib.parse

def send_data_to_models(path, data):
    url = "http://models:8000/api/v1/{}".format(path)

    post_data = data # No modifications

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
