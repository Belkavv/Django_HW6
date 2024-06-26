import logging
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Client, Product

logger = logging.getLogger(__name__)


def index(request):
    context = {"title": 'Главная страница'}
    logger.info('Index page accessed')
    return render(request, "hw3/index.html", context)


def client_orders(request, id_client: int):
    client = Client.objects.get(pk=id_client)

    # За последние 7 дней
    last_7_days = timezone.now() - timedelta(days=7)
    client_orders_last_7_days = Product.objects.filter(order__client=client,
                                                       order__order_date__gte=last_7_days).distinct()

    # За последние 30 дней
    last_30_days = timezone.now() - timedelta(days=30)
    client_orders_last_30_days = Product.objects.filter(order__client=client,
                                                        order__order_date__gte=last_30_days).distinct()

    # За последние 365 дней
    last_365_days = timezone.now() - timedelta(days=365)
    client_orders_last_365_days = Product.objects.filter(order__client=client,
                                                         order__order_date__gte=last_365_days).distinct()

    logger.debug('About page accessed')
    return render(request, 'hw3/client_order.html', {
        'client_orders_last_7_days': client_orders_last_7_days,
        'client_orders_last_30_days': client_orders_last_30_days,
        'client_orders_last_365_days': client_orders_last_365_days,
    })
