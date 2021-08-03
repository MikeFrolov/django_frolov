from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import Teacher


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('number_of_teachers', nargs='+', type=int, default=100)

    def handle(self, *args, **options):
        number = options['number_of_teachers']
        fake = Faker()
        for i in range(*number):
            Teacher.objects.create(first_name=fake.first_name(),
                                   last_name=fake.last_name(),
                                   age=fake.random_int(23, 85))
        self.stdout.write(self.style.SUCCESS(f'Successfully created {str(*number)} new teachers on the database'))
