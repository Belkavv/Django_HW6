from datetime import timedelta, date
from django.core.management.base import BaseCommand
from homework5.models import Order, Client, Product
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Populate the database with sample orders and related data'

    @staticmethod
    def random_date():
        start_date = date(2022, 1, 1)
        end_date = date(2024, 6, 26)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_number_of_days)
        return random_date

    def handle(self, *args, **options):
        # Создаем несколько клиентов
        clients = [Client.objects.create(
            name=f'Client {i}',
            email=f'client{i}@example.com',
            phone_number=f'12345678{i}',
            address=f'Street {i}'
        ) for i in range(1, 6)]

        # Создаем несколько товаров
        products = [Product.objects.create(
            name=f'Product {i}',
            description=f'Description for Product {i}',
            price=Decimal(random.uniform(10, 100)),
            quantity=random.randint(1, 10)
        ) for i in range(1, 11)]

        # Создаем несколько заказов и связанных продуктов
        for i in range(1, 6):
            client = random.choice(clients)
            products_in_order = random.sample(products, random.randint(1, 5))
            total_amount = sum(product.price * product.quantity for product in products_in_order)
            random_order_date = self.random_date()
            order = Order.objects.create(
                client=client,
                total_amount=total_amount,
                order_date=random_order_date
            )
            order.save()
            order.products.set(products_in_order)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample orders.'))
