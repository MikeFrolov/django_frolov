from django.http import HttpResponse

from .models import Teacher

from faker import Faker


def make_teacher() -> object():
    """Generate student and added him in DataBase"""
    fake = Faker()
    teacher = Teacher.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(),
                                     age=fake.random_int(23, 85))
    return teacher


def generate_teacher(request) -> HttpResponse:
    teacher = make_teacher()
    output = ''.join(f"<p>Created 1 student with id: {teacher.id}</p>"
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

    # TODO: Think about how not to get an error if a filter field is entered, but its value is not entered
