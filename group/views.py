from django.http import HttpResponse

from .models import Group


def list_groups(request):
    groups_list = Group.objects.all()
    output = ''.join(
        [f"<p>Group name: {group.group_name}, Faculty name: {group.faculty_name} - "
         f"group consists of {group.nos} students;</p>" for group in groups_list]
        )
    return HttpResponse(output)
