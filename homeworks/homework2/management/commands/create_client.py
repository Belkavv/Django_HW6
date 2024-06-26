from django.core.management import BaseCommand

from homework2.models import Client


class Command(BaseCommand):
    help = "Create client"

    def handle(self, *args, **kwargs):
        client = Client(
            name = 'Ivan',
            email = '123@mail.ru',
            phone_number = '123456789',
            address = 'Text',
        )
        client.save()
        self.stdout.write(f"Клиент: '{client.name}' добавлен в бд")