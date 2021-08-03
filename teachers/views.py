from django.http import HttpResponse

from .models import Teacher


def teachers_list(request):
    all_teachers = Teacher.objects.all()
    output = ''.join(
        [f"<p>Teacher {teacher.id}: {teacher.first_name} {teacher.last_name}, {teacher.age} years old;</p>"
         for teacher in all_teachers]
    )
    return HttpResponse(output)
