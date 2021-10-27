from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from my_libs import count_validator, make_fake_person

from .forms import GenerateStudentForm
from .models import Student
from .tasks import generate_students_with_form

age = (16, 50)


class ListStudentsView(ListView):
    template_name = 'students/list_students.html'

    def get(self, request, **kwargs):
        filter_parameters = {p: v for p, v in request.GET.items()}

        if not filter_parameters:  # If no filtering parameters are entered
            students = Student.objects.all()
            # messages.info(request, 'Use the address with: ?id=int&first_name=str&last_name=str&age=int'
            #                        ' parameters, to list filtered students from database by parameter.'
            #               )
        # TODO: Add pagination
        # FIXME: Crashes if using pagination, Conflicting requests '?page=1' and '?age = 1'
            # paginator = Paginator(students, 10)
            # page_number = request.GET.get('page')
            # page_obj = paginator.get_page(page_number)
        # FIXME: Crashes if trying to enter a filter that does not exist
        # TODO: Add filter name check
        else:
            students = [obj for obj in Student.objects.filter(**filter_parameters)]
        return render(request, self.template_name, {'students': students})  # List students from database
        # return render(request, self.template_name, {'students': page_obj})


class GenerateStudentView(LoginRequiredMixin, View):
    redirect_name = 'list-students'

    def get(self, request):
        make_fake_person.make_person(Student, age)
        return redirect(self.redirect_name)


class GenerateStudentsView(LoginRequiredMixin, View):
    redirect_name = 'list-students'

    def get(self, request):
        count = request.GET.get("count", )  # get a count from url
        if count_validator.count_valid(count).isdigit():
            for _ in range(int(count)):
                make_fake_person.make_person(Student, age)
            messages.success(request, '{} random students created with success!'.format(count))
            return redirect(self.redirect_name)
        else:
            error_message = count_validator.count_valid(count)
            message = {'error_cod': '-- Url parameters error --', 'error_message': '{}'.format(str(error_message))}
            return render(request, 'custom_error.html', message)


class CreateStudentFormView(LoginRequiredMixin, CreateView):

    template_name = 'students/create_student_form.html'
    model = Student
    fields = ['first_name', 'last_name', 'age', 'phone']
    success_url = reverse_lazy('list-students')


class EditStudentFormView(LoginRequiredMixin, UpdateView):
    template_name = 'students/edit_student_form.html'
    model = Student
    fields = ['first_name', 'last_name', 'age', 'phone']
    success_url = reverse_lazy('list-students')


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    template_name = 'students/student_confirm_delete.html'
    model = Student
    success_url = reverse_lazy('list-students')


class GenerateStudentsFormView(LoginRequiredMixin, View):
    form_class = GenerateStudentForm
    template_name = 'students/generate_students_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            total = form.cleaned_data.get('total', )
            generate_students_with_form.delay(total)
            messages.success(request, 'Generation of {} students was successful!'
                                      'Wait a moment and refresh this page.'.format(total))
            return redirect('list-students')

        return render(request, self.template_name, {'form': form})
