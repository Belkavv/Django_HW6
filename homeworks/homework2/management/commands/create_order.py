from django.core.management import BaseCommand

from homework2.models import Order, Client, Product


class Command(BaseCommand):
    help = "Create order"

    def handle(self, *args, **kwargs):
        order = Order(
            client = Client.objects.get(pk = 1),
            products = Product.objects.all()[:3],
            total_amounts = Order.calculate_total_amount(),
            category = 'Some category'
        )
        order.save()
        self.stdout.write(f"Заказ на сумму: '{order.order_print()}' создан.")