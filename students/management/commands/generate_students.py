from django.core.management.base import BaseCommand

from faker import Faker

from students.models import Student


class Command(BaseCommand):
    help = 'Generates random students base on input amount'

    def add_arguments(self, parser):
        parser.add_argument('number_of_students', nargs='+', type=int, default=100)

    def handle(self, *args, **options):
        number = options['number_of_students']
        fake = Faker()
        students = []
        for i in range(*number):
            Student.objects.create(first_name=fake.first_name(),
                                   last_name=fake.last_name(),
                                   age=fake.random_int(16, 45))
        self.stdout.write(self.style.SUCCESS(f'Successfully created {str(*number)} new students on the database'))
