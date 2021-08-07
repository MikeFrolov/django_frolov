from django.urls import path

from .views import (
    create_teacher_form,
    list_filtered_teachers
)


urlpatterns = [
    path('create_teacher_form/', create_teacher_form, name='create-teacher-form'),
    path('list_teachers/', list_filtered_teachers, name='list-filtered-teachers'),
]
