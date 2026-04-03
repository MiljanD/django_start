
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import FileExtensionValidator, MinLengthValidator
from .helpers.image_compressor import ImageCompressor
from django.contrib.auth.models import User



class Categories(models.Model):
    name = models.CharField(max_length=64, unique=True)
    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="products/", null=True,
                              validators=[FileExtensionValidator(allowed_extensions=[
                                  "jpg", "jpeg", "png", "webp"
                              ])])
    amount = models.PositiveIntegerField(default=0)
    promoted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)



    class Meta:
        db_table = "product"


    def __str__(self):
        return self.title

    def clean(self):
        if self.promoted_price and self.price:
            if self.promoted_price > self.price:
                raise ValidationError({
                    "promoted_price": "Promotion price needs to be lower than actual price."
                })

    def save(self, *args, **kwargs):
        if self.image:
            compressor = ImageCompressor()
            compressed = compressor.compress(self.image)
            self.image.save(f"{self.image.name.split(".")[0]}.webp", compressed, save=False)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", null=True)
    image = models.ImageField(upload_to="products/", null=True,
                              validators=[
                                  FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"])
                              ])

    def save(self, *args, **kwargs):
        if self.image:
            compressor = ImageCompressor()
            compressed = compressor.compress(self.image)
            self.image.save(f"{self.image.name.split(".")[0]}.webp", compressed, save=False)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Image for {self.product.title}"


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code = models.IntegerField()
    phone_number = models.CharField(max_length=36)

    class Meta:
        db_table = "orders"


class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="order")
    item = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "order_items"

