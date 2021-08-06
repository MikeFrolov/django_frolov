from django.http import HttpResponse
from django.shortcuts import render

from faker import Faker

from .forms import TeacherForm
from .models import Teacher


def make_teacher() -> object():
    """Generate teacher and added him in DataBase"""
    fake = Faker()
    teacher = Teacher.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(),
                                     age=fake.random_int(23, 85))
    return teacher


def create_teacher_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data form the request:
        form = TeacherForm(request.POST)
        # check form it's valid:
        if form.is_valid():
            Teacher.objects.create(**form.cleaned_data)
            teacher = Teacher.objects.last()

            return HttpResponse(''.join(f"<p>Created 1 teacher with id: {teacher.id}</p>"
                                f"<p>{teacher.first_name} {teacher.last_name}, {teacher.age};</p>"))

    # if this is a GET request or (any other method) we'll create a blank form
    else:
        form = TeacherForm()

    return render(request, 'create_teacher_form.html', {'form': form})


def generate_teacher(request) -> HttpResponse:
    teacher = make_teacher()
    output = ''.join(f"<p>Created 1 teacher with id: {teacher.id}</p>"
                     f"<p>{teacher.first_name} {teacher.last_name}, {teacher.age};</p>")
    return HttpResponse(output)


def list_all_teachers(request):
    """
    List all teachers from database
    :param request: None
    :return: HttpResponse
    """
    teachers_list = Teacher.objects.all()
    output = ''.join(
        [f"<p>Teacher {teacher.id}: {teacher.first_name} {teacher.last_name}, {teacher.age} years old;</p>"
         for teacher in teachers_list]
    )
    return HttpResponse(output)


def list_filtered_teachers(request):
    """
    List teachers with filtering functionality by fields age, first_name, last_name.
    :param request: id, first_name, last_name, age, discipline
    :return: HttpResponse
    """

    filter_parameters = {p: v for p, v in request.GET.items()}

    if not filter_parameters:  # If no filtering parameters are entered
        return list_all_teachers(request)  # List all teachers from database
    else:
        filtered_teachers = [obj for obj in Teacher.objects.filter(**filter_parameters)]

        output = ''.join(
            [f"<p>Teacher {teacher.id}: {teacher.first_name} {teacher.last_name}, {teacher.age} years old;</p>"
             for teacher in filtered_teachers])
        return HttpResponse(output)
