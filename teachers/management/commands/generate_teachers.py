from django.core.management.base import BaseCommand

from faker import Faker

import random

from teachers.views import make_teacher
from students.views import make_student
from groups.views import Group


class Command(BaseCommand):
    # help = 'Generates random students base on input amount'

    def add_arguments(self, parser):
        parser.add_argument('number_of_teachers', nargs='+', type=int, default=100)

    def handle(self, *args, **options):
        number = options['number_of_teachers']
        fake = Faker()
        for i in range(*number):
            teacher = make_teacher()
            students = [make_student() for _ in range(fake.random_int(1, 10))]
            headman = random.choice(students)
            group = Group.objects.create(
                group_name=f'group{(str(len(Group.objects.all()) + 1))}',
                curator=teacher,
                headman=headman)
            group.students.set(students)
            group.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created {str(*number)} new teachers on the database'))
