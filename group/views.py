from django.http import HttpResponse

from .models import Group


def groups_list(request):
    all_groups = Group.objects.all()
    output = ''.join(
        [f"<p>Group name: {group.group_name}, Faculty name: {group.faculty_name} - "
         f"group consists of {group.nos} students;</p>" for group in all_groups]
        )
    return HttpResponse(output)
