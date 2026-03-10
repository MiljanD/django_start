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

from django.conf import settings
from django.urls import re_path
from django.views.static import serve

from django.contrib import admin
from django.urls import path
from core.views.general import home
from core.views.general import about
from core.views.user import user

from core.views.product import product
from core.views.product import create_product
from core.views.product import save_product

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home),
    path('about/', about),
    path('proizvod/<str:name>', product, name='product_page'),
    path('korisnik/<int:uid>', user),
    path('admin/proizvod/create', create_product),
    path('admin/proizvod/save', save_product),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html', next_page='/'), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    re_path(r'media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    })
]
