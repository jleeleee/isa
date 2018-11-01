from django import forms
from django.http import HttpResponse

import urllib.request
import urllib.parse
import json

def send_to_exp(request, form, path):
    data = form.cleaned_data
    url = "http://exp:8000/api/v1/{}".format(path)

    post_data = data
    post_data["user_id"] = request.COOKIES.get('user_id')
    post_data["auth"] = request.COOKIES.get('auth')

    try:
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req, data=urllib.parse.urlencode(post_data).encode())
        resp_json = res.read().decode('utf-8')
        resp = json.loads(resp_json)
        return {
            "success": True,
            "response": resp
        }
    except urllib.error.HTTPError as e:
        return {
            "success": False,
            "response": str(e.reason)
        }

class ListingCreationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    generic_description = forms.CharField(required=False, widget=forms.Textarea)
    price = forms.DecimalField()
