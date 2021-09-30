from django.shortcuts import redirect, render


from .forms import GroupFormFormModel
from .models import Group


def list_groups(request):
    groups_list = Group.objects.all()
    return render(request, 'list_groups.html', {'groups': groups_list})  # List all groups from database


def create_group_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data form the request:
        form = GroupFormFormModel(request.POST)
        # check form it's valid:
        if form.is_valid():
            groups = Group.objects.create(
                group_name=form.cleaned_data["group_name"],
                discipline=form.cleaned_data["discipline"],
                curator=form.cleaned_data["curator"],
                headman=form.cleaned_data["headman"],
            )

            for student in form.cleaned_data['students']:
                groups.students.add(student)

            return redirect('list-groups')
    else:
        form = GroupFormFormModel()

    return render(request, 'create_group_form.html', {'form': form})


def edit_group_form(request, group_id):
    # TODO: How to change students, curator and headman?
    if request.method == 'POST':
        form = GroupFormFormModel(request.POST)
        if form.is_valid():
            group = Group.objects.filter(id=group_id)
            group.delete()
            groups = Group.objects.create(
                group_name=form.cleaned_data["group_name"],
                discipline=form.cleaned_data["discipline"],
                curator=form.cleaned_data["curator"],
                headman=form.cleaned_data["headman"],
            )

            for student in form.cleaned_data['students']:
                groups.students.add(student)
            return redirect('list-groups')
    else:
        group = Group.objects.filter(id=group_id).first()
        form = GroupFormFormModel(instance=group)

    return render(request, 'edit_group_form.html', {'form': form, 'group_id': group_id})


def delete_group(request, group_id):
    group = Group.objects.filter(id=group_id)
    group.delete()
    return redirect('list-groups')
