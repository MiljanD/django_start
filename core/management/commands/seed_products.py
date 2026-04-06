
from django.core.management.base import BaseCommand
from faker import Faker
from core.models import Product, Categories


class Command(BaseCommand):

    help = "Seed database with dummy products"

    def handle(self, *args, **options):

        fake = Faker()

        for _ in range(20):
            Product.objects.create(
                title=fake.word(),
                price=round(fake.random_number(digits=3), 2),
                description=fake.sentence(),
                category=Categories.objects.get(id=1),
                image="products/smile1.jpg",
                amount=fake.random_number(digits=2)
            )

        self.stdout.write(self.style.SUCCESS("Added products to database"))

