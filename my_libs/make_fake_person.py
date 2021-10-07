from faker import Faker

from my_libs import phone_generator


def make_person(model, age):
    """Generate person and added him in the DataBase"""
    fake = Faker()
    person = model.objects.create(first_name=(fake.first_name()),
                                  last_name=fake.last_name(),
                                  age=fake.random_int(*age),
                                  phone=phone_generator.phone_generate())
    return person
