from django.urls import path

from . import views


urlpatterns = [
    path('generate-student/', views.generate_student, name='generate-student'),
    path('generate-students/', views.generate_students, name='generate-students'),
    path('create_student_form/', views.create_student_form, name='create-student-form'),
    path('list_students/', views.list_filtered_students, name='list-filtered-students'),
]
