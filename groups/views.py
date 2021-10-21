from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from .forms import GroupFormFormModel
from .models import Group


class GroupsListView(ListView):
    model = Group
    template_name = 'groups/list_groups.html'


class CreateGroupFormView(View):
    template_name = 'groups/create_group_form.html'
    form_class = GroupFormFormModel

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

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

        return render(request, self.template_name, {'form': form})


class EditGroupFormView(View):
    template_name = 'groups/edit_group_form.html'
    form_class = GroupFormFormModel

    def get(self, request, *args, **kwargs):
        group = Group.objects.filter(id=kwargs['group_id']).first()
        form = GroupFormFormModel(instance=group)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():  # If form valid:
            # To the variable group, assign the filtered group by ID from the database
            group = Group.objects.filter(id=kwargs['group_id']).first()

            group.group_name = form.cleaned_data["group_name"]  # Update object 'group_name' field
            group.discipline = form.cleaned_data["discipline"]  # Update object 'discipline' field
            group.curator = form.cleaned_data["curator"]  # Update object 'curator' field
            group.headman = form.cleaned_data["headman"]  # Update object 'headman' field
            group.save()  # Save all changes in object fields

            group.students.clear()  # clean all the many-to-many relationships of the object field 'students'
            group.save()  # Save all changes in object fields

            # Add new links from the form.list to the object field 'students' one by one
            for student in form.cleaned_data['students']:
                group.students.add(student)

            return redirect('list-groups')

        return render(request, self.template_name, {'form': form})


class DeleteGroupView(DeleteView):
    template_name = 'groups/group_confirm_delete.html'
    model = Group
    success_url = reverse_lazy('list-groups')
