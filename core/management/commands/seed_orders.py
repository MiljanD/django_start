
from random import randint
from django.core.management.base import BaseCommand
from faker import Faker
from core.models import Orders, OrderItems, Product
from django.contrib.auth.models import User


class Command(BaseCommand):

    help = "Seed database with dummy products"

    def handle(self, *args, **options):

        fake = Faker()

        for _ in range(6):
            new_order = Orders.objects.create(
                name=fake.name_nonbinary(),
                country=fake.country(),
                city=fake.city(),
                postal_code=fake.random_number(digits=6),
                phone_number=fake.phone_number(),
                user=User.objects.get(id=3)
            )
            new_qty = fake.random_number(digits=2)
            product_id = randint(3, 20)
            total_price = Product.objects.get(id=product_id).price * new_qty
            OrderItems.objects.create(
                item=Product.objects.get(id=product_id).title,
                quantity=new_qty,
                price=total_price,
                order=new_order
            )

        self.stdout.write(self.style.SUCCESS("Added orders and order items to database"))

