from django.http import HttpResponse

from .models import Teacher


def teachers(request):
    teachers_list = Teacher.objects.all()
    output = ''.join(
        [f"<p>Teacher {teacher.id}: {teacher.first_name} {teacher.last_name} - "
         f"teaches: '{teacher.discipline}' course;</p>" for teacher in teachers_list]
    )
    return HttpResponse(output)
