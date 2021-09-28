from django.http import HttpResponse
from django.shortcuts import redirect, render

from faker import Faker

from my_libs import count_validator, phone_generator

from .forms import TeacherFormFormModel
from .models import Teacher


def list_filtered_teachers(request):

    filter_parameters = {p: v for p, v in request.GET.items()}
    teachers_list = Teacher.objects.all()

    if not filter_parameters:  # If no filtering parameters are entered
        return render(request, 'list_teachers.html', {'teachers': teachers_list})  # List all teachers from database
    else:
        list_teacher = [obj for obj in Teacher.objects.filter(**filter_parameters)]
        return render(request, 'list_filtered_teachers.html', {'teachers': list_teacher})


def make_teacher():
    """Generate student and added him in DataBase"""
    fake = Faker()
    student = Teacher.objects.create(first_name=(fake.first_name()),
                                     last_name=fake.last_name(),
                                     age=fake.random_int(33, 99),
                                     phone=phone_generator.phone_generate())

    return student


def generate_teacher(request):
    make_teacher()
    return redirect('list-filtered-teachers')


def generate_teachers(request, teacher_number=100):
    count = request.GET.get("count", "")  # get a count from url
    if count_validator.count_valid(count).isdigit():
        for i in range(int(count)):
            fake = Faker()
            Teacher.objects.create(first_name=fake.first_name(),
                                   last_name=fake.last_name(),
                                   age=fake.random_int(23, 99),
                                   phone=phone_generator.phone_generate())

        return redirect('list-filtered-teachers')
    else:
        return HttpResponse(count_validator.count_valid(count))


def create_teacher_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data form the request:
        form = TeacherFormFormModel(request.POST)
        # check form it's valid:
        if form.is_valid():
            Teacher.objects.create(**form.cleaned_data)
            return redirect('list-filtered-teachers')
    else:
        form = TeacherFormFormModel()

    return render(request, 'create_teacher_form.html', {'form': form})


def edit_teacher_form(request, teacher_id):
    if request.method == 'POST':
        form = TeacherFormFormModel(request.POST)
        if form.is_valid():
            Teacher.objects.update_or_create(defaults=form.cleaned_data, id=teacher_id)
            return redirect('list-filtered-teachers')
    else:
        teacher = Teacher.objects.filter(id=teacher_id).first()
        form = TeacherFormFormModel(instance=teacher)

    return render(request, 'edit_teacher_form.html', {'form': form, 'teacher_id': teacher_id})


def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.filter(id=teacher_id)
    teacher.delete()
    return redirect('list-filtered-teachers')
