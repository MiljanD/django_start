from django.contrib import admin
from .models import Product, Categories
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "in_stock","price", "image_preview"]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50">', obj.image.url)
        return "Ne postoji"

    def in_stock(self, obj):
        return "Yes" if obj.amount else "No"


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Categories)


