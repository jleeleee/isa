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
from django.conf.urls.static import static
from django.conf import settings

from .apps.base import views as base

urlpatterns = [
    path('', base.index, name="homepage"),
    path('register', base.register, name="register"),
    path('login', base.login, name="login"),
    path('logout', base.logout, name="logout"),
    path('listings/<int:_id>', base.listing, name="listing"),
    path('listings/create', base.listing_create, name="create_listing"),
    path('listings/search', base.listing_search, name="search_listing"),
    path('listings', base.listing_index, name="listings"),
    path('about', base.about, name="about")
]  + static(settings.STATIC_URL, document_root="partex/static")
