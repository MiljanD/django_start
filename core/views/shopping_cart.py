
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Product
from django.contrib.auth.decorators import login_required


@login_required(login_url="login_page")
def add_to_cart(request, product_id):
    cart = request.session.get("shopping_cart", {})

    get_object_or_404(Product, id=product_id)

    product_id = str(product_id)
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session["shopping_cart"] = cart
    request.session.modified = True

    return redirect("cart_details")



@login_required(login_url="login_page")
def delete_from_cart(request, product_id):
    cart = request.session.get("shopping_cart", {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session["shopping_cart"] = cart
    request.session.modified = True

    return redirect("cart_details")


def show_cart(request):
    cart = request.session.get("shopping_cart", {})
    items = []
    total_cart = 0
    for product_id, quantity in cart.items():

        selected_product = Product.objects.get(id=int(product_id))

        total_price = quantity * (
            selected_product.promoted_price if selected_product.promoted_price else selected_product.price)
        total_cart += total_price

        items.append({
            "product": selected_product,
            "quantity": quantity,
            "total_price": total_price
        })

    return render(request, "shopping_cart.html", {"items": items, "total_cart": total_cart})