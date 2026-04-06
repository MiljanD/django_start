from django.http import HttpResponse
from django.shortcuts import render
from ..models import Product



def home(request):
    return render(request, "index.html", {"all": Product.objects.order_by("-id")})


def about(request):
    return HttpResponse("An error happened while served this page", status=404)
