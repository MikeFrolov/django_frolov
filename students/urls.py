from django.urls import path

from .views import (
    create_student_form,
    edit_student_form,
    generate_student,
    generate_students,
    list_filtered_students
)


urlpatterns = [
    path('generate-student/', generate_student, name='generate-student'),
    path('generate-students/', generate_students, name='generate-students'),
    path('create_student_form/', create_student_form, name='create-student-form'),
    path('edit_student_form/<int:student_id>', edit_student_form, name='edit-student-form'),
    path('list_students/', list_filtered_students, name='list-filtered-students'),


]
