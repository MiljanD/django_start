"""
URL configuration for prviprojekat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from core.views import home
from core.views import about
from core.views import product
from core.views import user
from core.views import create_product
from core.views import save_product

urlpatterns = [
    path('', home),
    path('about/', about),
    path('proizvod/<str:name>', product),
    path('korisnik/<int:uid>', user),
    path('admin/proizvod/create', create_product),
    path('admin/proizvod/save', save_product)
]
