from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "test": "meme"
    }
    render("index.html", context)
