from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from faker import Faker

from my_libs import count_validator

from .forms import StudentFormFormModel
from .models import Student


def list_filtered_students(request):

    filter_parameters = {p: v for p, v in request.GET.items()}
    students_list = Student.objects.all()

    if not filter_parameters:  # If no filtering parameters are entered
        return render(request, 'list_students.html', {'students': students_list})  # List all students from database
    else:
        list_students = [obj for obj in Student.objects.filter(**filter_parameters)]
        return render(request, 'list_filtered_students.html', {'students': list_students})


def make_student():
    """Generate student and added him in DataBase"""
    fake = Faker()
    student = Student.objects.create(first_name=fake.first_name(),
                                     last_name=fake.last_name(),
                                     age=fake.random_int(16, 45))
    return student


def generate_student(request):
    make_student()
    return HttpResponseRedirect(reverse('list-filtered-students'))


def generate_students(request, student_number=100):
    count = request.GET.get("count", "")  # get a count from url
    if count_validator.count_valid(count).isdigit():
        for i in range(int(count)):
            make_student()
        return HttpResponseRedirect(reverse('list-filtered-students'))
    else:
        return HttpResponse(count_validator.count_valid(count))


def create_student_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data form the request:
        form = StudentFormFormModel(request.POST)
        # check form it's valid:
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
        return HttpResponseRedirect(reverse('list-filtered-students'))

    # if this is a GET request or (any other method) we'll create a blank form
    else:
        form = StudentFormFormModel()

    return render(request, 'create_student_form.html', {'form': form})


def edit_student_form(request, student_id):
    if request.method == 'POST':
        form = StudentFormFormModel(request.POST)
        if form.is_valid():
            Student.objects.update_or_create(defaults=form.cleaned_data, id=student_id)
            return HttpResponseRedirect(reverse('list-filtered-students'))
    else:
        student = Student.objects.filter(id=student_id).first()
        form = StudentFormFormModel(instance=student)

    return render(request, 'edit_student_form.html', {'form': form, 'student_id': student_id})


def delete_student(request, student_id):
    student = Student.objects.filter(id=student_id)
    student.delete()
    return HttpResponseRedirect(reverse('list-filtered-students'))
