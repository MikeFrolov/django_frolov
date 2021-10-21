from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from my_libs import count_validator, make_fake_person

from .models import Teacher

age = (23, 90)


class ListTeachersView(View):
    template_name = 'teachers/list_teachers.html'

    def get(self, request):
        filter_parameters = {p: v for p, v in request.GET.items()}

        if not filter_parameters:  # If no filtering parameters are entered
            teachers_list = Teacher.objects.all()
            messages.info(request, 'Use the address with: ?id=int&first_name=str&last_name=str&age=int'
                                   ' parameters, to list filtered teachers from database by parameter.'
                          )
        else:
            teachers_list = [obj for obj in Teacher.objects.filter(**filter_parameters)]
        return render(request, self.template_name, {'teachers': teachers_list})  # List teachers from database


class GenerateTeacherView(View):
    redirect_name = 'list-teachers'

    def get(self, request):
        make_fake_person.make_person(Teacher, age)
        return redirect(self.redirect_name)


class GenerateTeachersView(View):
    redirect_name = 'list-teachers'

    def get(self, request):
        count = request.GET.get("count", "")  # get a count from url
        if count_validator.count_valid(count).isdigit():
            for _ in range(int(count)):
                make_fake_person.make_person(Teacher, age)
            messages.success(request, '{} random teachers created with success!'.format(count))
            return redirect(self.redirect_name)
        else:
            error_message = count_validator.count_valid(count)
            message = {'error_cod': '-- Url parameters error --', 'error_message': '{}'.format(str(error_message))}
            return render(request, 'custom_error.html', message)


class CreateTeacherFormView(CreateView):
    template_name = 'teachers/create_teacher_form.html'
    model = Teacher
    fields = ['first_name', 'last_name', 'age', 'phone']
    success_url = reverse_lazy('list-teachers')


class EditTeacherFormView(UpdateView):
    template_name = 'teachers/edit_teacher_form.html'
    model = Teacher
    fields = ['first_name', 'last_name', 'age', 'phone']
    success_url = reverse_lazy('list-teachers')


class DeleteTeacherView(DeleteView):
    model = Teacher
    template_name = 'teachers/teacher_confirm_delete.html'
    success_url = reverse_lazy('list-teachers')


# def list_filtered_teachers(request):
#
#     filter_parameters = {p: v for p, v in request.GET.items()}
#     teachers_list = Teacher.objects.all()
#
#     if not filter_parameters:  # If no filtering parameters are entered
#         return render(request, 'teachers/list_teachers.html', {'teachers': teachers_list})
#     else:
#         list_teacher = [obj for obj in Teacher.objects.filter(**filter_parameters)]
#         return render(request, 'teachers/list_teachers.html', {'teachers': list_teacher})


# def make_teacher():
#     """Generate teacher and added him in DataBase"""
#     fake = Faker()
#     teacher = Teacher.objects.create(first_name=(fake.first_name()),
#                                      last_name=fake.last_name(),
#                                      age=fake.random_int(33, 99),
#                                      phone=phone_generator.phone_generate())
#
#     return teacher


# def generate_teacher(request):
#     make_teacher()
#     return redirect('list-teachers')


# def generate_teachers(request, teacher_number=100):
#     count = request.GET.get("count", "")  # get a count from url
#     if count_validator.count_valid(count).isdigit():
#         for i in range(int(count)):
#             fake = Faker()
#             Teacher.objects.create(first_name=fake.first_name(),
#                                    last_name=fake.last_name(),
#                                    age=fake.random_int(23, 99),
#                                    phone=phone_generator.phone_generate())
#
#         return redirect('list-teachers')
#     else:
#         return HttpResponse(count_validator.count_valid(count))


# def create_teacher_form(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data form the request:
#         form = TeacherFormFormModel(request.POST)
#         # check form it's valid:
#         if form.is_valid():
#             Teacher.objects.create(**form.cleaned_data)
#             return redirect('list-teachers')
#     else:
#         form = TeacherFormFormModel()
#
#     return render(request, 'teachers/create_teacher_form.html', {'form': form})


# def edit_teacher_form(request, teacher_id):
#     if request.method == 'POST':
#         form = TeacherFormFormModel(request.POST)
#         if form.is_valid():
#             Teacher.objects.update_or_create(defaults=form.cleaned_data, id=teacher_id)
#             return redirect('list-teachers')
#     else:
#         teacher = Teacher.objects.filter(id=teacher_id).first()
#         form = TeacherFormFormModel(instance=teacher)
#
#     return render(request, 'teachers/edit_teacher_form.html', {'form': form, 'teacher_id': teacher_id})
#
#
# def delete_teacher(request, teacher_id):
#     teacher = Teacher.objects.filter(id=teacher_id)
#     teacher.delete()
#     return redirect('list-teachers')
