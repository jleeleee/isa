from django.shortcuts import render

from elasticsearch import Elasticsearch

import urllib.request
import urllib.parse
import json

# Create your views here.

def listings(request):
    es = Elasticsearch(['es'])
    res = es.search(index='listing_index', body = {
        'query': {
            'query_string': {
                'query': request.POST.get('q')
            },
        },
        'size': 10
    })
    if res['timed_out']:
        return JsonResponse({
            "ok": False,
            "response": res
        })

    hits = [ h["_source"] for h in res["hits"] ]
    return JsonResponse({
        "ok": True,
        "response": hits
    })
