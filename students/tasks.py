from celery import shared_task

from faker import Faker

from my_libs import phone_generator

from .models import Student


@shared_task
def generate_students_with_form(total):
    fake = Faker()
    result = []

    for _ in range(total):
        result.append(Student(
            first_name=(fake.first_name()),
            last_name=fake.last_name(),
            age=fake.random_int(16, 45),
            phone=phone_generator.phone_generate()
        ))
    Student.objects.bulk_create(result)

    return '{} random students created with success!'.format(total)
