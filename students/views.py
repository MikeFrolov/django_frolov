from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker

from .models import Student
from .forms import StudentForm

from my_libs import count_validator


def make_student() -> object():
    """Generate student and added him in DataBase"""
    fake = Faker()
    student = Student.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(),
                                     age=fake.random_int(16, 45))
    return student


def create_student_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data form the request:
        form = StudentForm(request.POST)
        # check form it's valid:
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponse('Student creation was successful!')
    # if this is a GET request or (any other method) we'll create a blank form
    else:
        form = StudentForm()

    return render(request, 'student.html', {'form': form})


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
    if count_validator.count_valid(count).isdigit():
        for i in range(int(count)):
            student = make_student()
            new_students.append(student)

        output = [f"<p>Created new student: {x.id} {x.first_name} {x.last_name}, {x.age};</p>" for x in new_students]
        return HttpResponse(output)
    else:
        return HttpResponse(count_validator.count_valid(count))


def list_all_students(request):
    """
    List all students from database
    :param request: None
    :return: HttpResponse
    """
    students_list = Student.objects.all()
    output = ''.join(
        [f"<p>Student {student.id}: {student.first_name} {student.last_name}, {student.age} years old;</p>"
         for student in students_list]
    )
    return HttpResponse(output)


def list_filtered_students(request):
    """
    List students with filtering functionality by fields age, first_name, last_name.
    :param request: id, first_name, last_name, age, discipline
    :return: HttpResponse
    """

    filter_parameters = {p: v for p, v in request.GET.items()}

    if not filter_parameters:  # If no filtering parameters are entered
        return list_all_students(request)  # List all students from database
    else:
        filtered_students = [obj for obj in Student.objects.filter(**filter_parameters)]

        output = ''.join(
            [f"<p>Student {student.id}: {student.first_name} {student.last_name}, {student.age} years old;</p>"
             for student in filtered_students])
        return HttpResponse(output)
