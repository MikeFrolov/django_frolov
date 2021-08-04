from django.http import HttpResponse
from django.shortcuts import render

from .forms import GroupFormFormModel
from .models import Group


def create_group_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data form the request:
        form = GroupFormFormModel(request.POST)
        # check form it's valid:
        if form.is_valid():
            Group.objects.create(**form.cleaned_data)
            group = Group.objects.last()

            return HttpResponse(''.join(f"<h4>Created new group with id: {group.id}</h4>"
                                        f"<p>Group name: {group.group_name};</p>"
                                        f"<p> Faculty name: {group.faculty_name};</p>"
                                        f"<p>Group consists of {group.number_of_students} students;</p>"))

    # if this is a GET request or (any other method) we'll create a blank form
    else:
        form = GroupFormFormModel()

    return render(request, 'group.html', {'form': form})


def list_groups(request):
    groups_list = Group.objects.all()
    output = ''.join(
        [f"<p>Group name: {group.group_name}, Faculty name: {group.faculty_name} - "
         f"group consists of {group.number_of_students} students;</p>" for group in groups_list]
        )
    return HttpResponse(output)
