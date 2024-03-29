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
from django.urls import path

from . import views

urlpatterns = [
    path('create', views.create),
    path('<int:id_>/delete', views.delete),
    path('<int:id_>/update', views.update),
    path('<int:id_>/recommendations', views.recommendations),
    path('<int:id_>', views.info),

    path('base/create', views.create_abstract),
    path('base/<int:id_>/delete', views.create_abstract),
    path('base/<int:id_>/update', views.create_abstract),

    path('recent', views.get_three_listings),

    path('', views.index)
]
