from django.urls import path

from .views import (
    create_teacher_form,
    delete_teacher,
    edit_teacher_form,
    generate_teacher,
    generate_teachers,
    list_filtered_teachers,

)


urlpatterns = [
    path('list_teachers/', list_filtered_teachers, name='list-filtered-teachers'),
    path('generate-teacher/', generate_teacher, name='generate-teacher'),
    path('generate-teachers/', generate_teachers, name='generate-teachers'),
    path('create_teacher_form/', create_teacher_form, name='create-teacher-form'),
    path('edit_teacher_form/<int:teacher_id>', edit_teacher_form, name='edit-teacher-form'),
    path('delete_teacher/<int:teacher_id>', delete_teacher, name='delete-teacher'),
]
