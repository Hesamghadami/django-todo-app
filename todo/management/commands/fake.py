
from django.core.management import BaseCommand
from faker import Faker
from ...models import Task
from accounts.models import CustomeUser
from random import choice


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker()

    def handle(self, *args, **options):
        for _ in range(10):
            task = Task.objects.get_or_create(
                user = CustomeUser.objects.get(id=1),
                title = self.faker.name(),
                complete = choice([True,False]),
            )
