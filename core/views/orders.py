
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from ..models import Product, Orders, OrderItems
from django.contrib.auth.decorators import login_required
from core.forms.order_form import OrderForm


@login_required(login_url="login_page")
def order_creation(request):
    order_form = OrderForm(initial={
        "name": request.user.get_full_name()
    })
    return render(request, "create_order.html", {"order_form": order_form})

@login_required(login_url="login_page")
def save_order(request):
    if request.method != "POST":
        return HttpResponseNotAllowed("This method is not allowed.")

    cart = request.session.get("shopping_cart", {})

    order_form = OrderForm(request.POST)
    if not order_form.is_valid():
        return redirect("create_order")


    user = request.user
    name = request.POST.get("name")
    country = request.POST.get("country")
    city = request.POST.get("city")
    postal_code = request.POST.get("postal_code")
    phone_number = request.POST.get("phone_number")



    new_order = Orders.objects.create(user=user, name=name, country=country, city=city, postal_code=postal_code, phone_number=phone_number)

    for product_id, quantity in cart.items():
        selected_product = Product.objects.get(id=int(product_id))

        total_price = quantity * (
            selected_product.promoted_price if selected_product.promoted_price else selected_product.price)

        OrderItems.objects.create(order=new_order, item=selected_product.title, quantity=quantity ,price=total_price)

    request.session["shopping_cart"] = {}
    request.session.modified = True

    return redirect("user_orders")


@login_required(login_url="login_page")
def show_user_orders(request):
    orders = Orders.objects.filter(user_id=request.user.id)
    order_data = []
    for order in orders:
        order_items = OrderItems.objects.filter(order_id=order.id)
        order_data.append({"order": order, "items": order_items})

    return render(request, "user_orders.html", {"orders": order_data})


