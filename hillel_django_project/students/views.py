from django.http import HttpResponse
from faker import Faker

from .models import Student, Group, Teacher


def count_valid(count):
    if not count:
        return HttpResponse('<p>Count not entered!</p>'
                            '<p>No new student has been created in the database</p>')
    if isinstance(count, str):
        try:
            int(count)
        except ValueError:
            return HttpResponse('<p>Count must be an integer!</p>'
                                '<p>No new student has been created in the database</p>')
        else:
            if 1 > int(count) or int(count) > 100:
                return HttpResponse('<p>Count must bу greater than 0 and no greater than 100</p>'
                                    '<p>No new student has been created in the database</p>')
        return int(count)


def make_student():
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
    if type(count_valid(count)) == int:
        for i in range(int(count)):
            student = make_student()
            new_students.append(student)

        output = [f"<p>Created new student: {x.id} {x.first_name} {x.last_name}, {x.age};</p>" for x in new_students]
        return HttpResponse(output)
    else:
        return count_valid(count)


def groups(request):
    groups_list = Group.objects.all()
    output = ''.join(
        [f"<p>Group name: {group.group_name}, Faculty name: {group.faculty_name} - "
         f"group consists of {group.nos} students;</p>" for group in groups_list]
        )
    return HttpResponse(output)


def teachers(request):
    teachers_list = Teacher.objects.all()
    output = ''.join(
        [f"<p>Teacher {teacher.id}: {teacher.first_name} {teacher.last_name} - "
         f"teaches: '{teacher.discipline}' course;</p>" for teacher in teachers_list]
    )
    return HttpResponse(output)
