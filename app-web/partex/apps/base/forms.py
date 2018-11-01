from django import forms

import urllib.request
import urllib.parse
import json

def send_to_exp(path, form):
    data = form.cleaned_data
    url = "http://exp:8000/api/v1/{}".format(path)

    post_data = data # No modifications

    try:
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req, urllib.urlencode(post_data))
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
    generic_description = forms.CharField(required=False, widget=forms.TextArea)
