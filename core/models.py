from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=64, unique=True)
    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "product"




