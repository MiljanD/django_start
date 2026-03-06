from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

products = {
    "Mac Air 2025": {
        "price": 2000,
        "description": "This is MacBook Air 2025",
    },
    "Dell XPS 15": {
        "price": 1800,
        "description": "High-performance Dell XPS 15 laptop",
    },
    "iPhone 16 Pro": {
        "price": 1200,
        "description": "Apple iPhone 16 Pro smartphone",
    },
    "Samsung Galaxy S25": {
        "price": 1100,
        "description": "Samsung Galaxy S25 flagship phone",
    },
    "Sony WH-1000XM6": {
        "price": 450,
        "description": "Sony WH-1000XM6 noise-cancelling headphones",
    },
}

def home(request):
    contex = {
        "all": products
    }
    return render(request, "index.html", contex)


def about(request):
    return HttpResponse("An error happened while served this page", status=404)

def product(request, name):
    chosen_product = products.get(name)
    if not chosen_product:
        return HttpResponseNotFound(f"Chosen product is not in list.")

    contex = {
        "name": name,
        "product": chosen_product
    }
    return render(request, "product.html", contex)


def user(request, uid):
    return HttpResponse(f"User id: {uid}")