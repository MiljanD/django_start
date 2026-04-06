

from django.shortcuts import redirect
from django.urls import reverse


class CartCheckMiddleware:

    protected_urls = [
        '/orders/create_order',
        '/orders/save_order'
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        if path in self.protected_urls:
            cart = request.session.get("shopping_cart", {})
            if not cart:
                return redirect(reverse('cart_details'))

        response = self.get_response(request)
        return response