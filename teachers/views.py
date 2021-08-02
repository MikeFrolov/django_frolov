from django.http import HttpResponse

from .models import Teacher


def get_all_teachers(request):
    """
    List all teachers from database
    :param request: None
    :return: HttpResponse
    """
    teachers_list = Teacher.objects.all()
    output = ''.join(
        [f"<p>Teacher {teacher.id}: {teacher.first_name} {teacher.last_name}, {teacher.age} years old - "
         f"teaches: '{teacher.discipline}' course;</p>" for teacher in teachers_list]
    )
    return HttpResponse(output)


def get_filtered_teachers(request):
    """
    List teachers with filtering functionality by fields age, first_name, last_name.
    :param request: id, first_name, last_name, age, discipline
    :return: HttpResponse
    """

    filter_parameters = {p: v for p, v in request.GET.items()}

    if not filter_parameters:  # If no filtering parameters are entered
        return get_all_teachers(request)  # List all teachers from database
    else:
        filtered_teachers = [obj for obj in Teacher.objects.filter(**filter_parameters)]

        output = ''.join(
            [f"<p>Teacher {teacher.id}: {teacher.first_name} {teacher.last_name}, {teacher.age} years old - "
             f"teaches: '{teacher.discipline}' course;</p>" for teacher in filtered_teachers])
        return HttpResponse(output)

    # TODO: Think about how not to get an error if a filter field is entered, but its value is not entered
