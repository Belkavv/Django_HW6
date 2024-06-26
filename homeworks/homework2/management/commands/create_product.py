from django.core.management import BaseCommand

from homework2.models import Product


class Command(BaseCommand):
    help = "Create product"

    def handle(self, *args, **kwargs):
        product = Product(
            name = 'Name',
            description = 'Text',
            price = '1000',
            quantity = '5',
        )
        product.save()
        self.stdout.write(f"Товар: '{product.name}' добавлен в бд")