from django.http import HttpResponse
from faker import Faker

from .models import Student


def count_valid(count) -> str:
    if not count:
        return '<p>Count not entered!</p>'
    if isinstance(count, str):
        try:
            int(count)
        except ValueError:
            return '<p>Count must be an integer!</p>'
        else:
            if 1 > int(count) or int(count) > 100:
                return '<p>Count must bу greater than 0 and no greater than 100</p>'

        return str(count)


def make_student() -> object():
    # Todo: Think about: What returned this function?
    """Generate student and added him in DataBase"""
    fake = Faker()
    student = Student.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(),
                                     age=fake.random_int(16, 45))
    return student


def home(request) -> HttpResponse:
    return HttpResponse('<h1 align=center>Welcome to "Hillel Homework Django Project"</h1>'
                        '<p align=center>by Michail Frolov</p>')


def generate_student(request) -> HttpResponse:
    student = make_student()
    output = ''.join(f"<p>Created 1 student with id: {student.id}</p>"
                     f"<p>{student.first_name} {student.last_name}, {student.age};</p>")
    return HttpResponse(output)


def generate_students(request) -> HttpResponse:
    count = request.GET.get("count", "")  # get a count from url
    new_students = []
    if count_valid(count).isdigit():
        for i in range(int(count)):
            student = make_student()
            new_students.append(student)

        output = [f"<p>Created new student: {x.id} {x.first_name} {x.last_name}, {x.age};</p>" for x in new_students]
        return HttpResponse(output)
    else:
        return HttpResponse(count_valid(count))
