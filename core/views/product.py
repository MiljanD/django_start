from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.shortcuts import render
from ..models import Product, Orders


def product(request, name):
    try:
        chosen_product = Product.objects.get(title=name)
        return render(request, "product.html", {"product": chosen_product})
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product don't exists", status=400)

@login_required
def create_product(request):
    return render(request, "product_create.html")


def save_product(request):
    if request.method != "POST":
        return HttpResponseNotAllowed("This method is not allowed")

    title = request.POST.get("title")
    price = request.POST.get("price")
    description = request.POST.get("description")

    if not title or not price or not description:
        return HttpResponse("All fields are mandatory.", status=400) # 400 -->> Bad request

    new_product = Product(title=title, price=price, description=description)
    new_product.save()

    return HttpResponse(f"This is {title}, {price}, {description}", status=201)



