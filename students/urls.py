from django.urls import path

from . import views


urlpatterns = [
    path('generate-student/', views.generate_student),
    path('generate-students/', views.generate_students),
    path('create_student_form/', views.create_student_form),
    path('list_students/', views.list_filtered_students),
]
