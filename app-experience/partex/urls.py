"""partex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .apps.base import views
from .apps.search import views as search

apipatterns = [
    path('home', views.homepage),
    path('all_listings', views.all_listings),
    path('listings/<int:_id>', views.listing),
    path('listings/create', views.create_listing),
    path('listings/search', search.listings),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout)
]

urlpatterns = [
    path('api/v1/', include(apipatterns))
]
