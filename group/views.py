from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


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
            Group.objects.create(**form.cleaned_data)

            return HttpResponseRedirect(reverse('list-groups'))
    else:
        form = GroupFormFormModel()

    return render(request, 'create_group_form.html', {'form': form})


def edit_group_form(request, group_id):
    if request.method == 'POST':
        form = GroupFormFormModel(request.POST)
        if form.is_valid():
            Group.objects.update_or_create(defaults=form.cleaned_data, id=group_id)
            return HttpResponseRedirect(reverse('list-groups'))
    else:
        group = Group.objects.filter(id=group_id).first()
        form = GroupFormFormModel(instance=group)

    return render(request, 'edit_group_form.html', {'form': form, 'group_id': group_id})


def delete_group(request, group_id):
    group = Group.objects.filter(id=group_id)
    group.delete()
    return HttpResponseRedirect(reverse('list-groups'))
