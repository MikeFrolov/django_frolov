from django.urls import path

from .views import (
    CreateStudentFormView,
    DeleteStudentView,
    EditStudentFormView,
    GenerateStudentView,
    GenerateStudentsFormView,
    GenerateStudentsView,
    ListStudentsView,
)


urlpatterns = [
    path('list_students/', ListStudentsView.as_view(), name='list-students'),
    path('generate-student/', GenerateStudentView.as_view(), name='generate-student'),
    path('generate-students/', GenerateStudentsView.as_view(), name='generate-students'),
    path('generate_students_form/', GenerateStudentsFormView.as_view(), name='generate-students-form'),
    path('create_student_form/', CreateStudentFormView.as_view(), name='create-student-form'),
    path('edit_student_form/<int:pk>', EditStudentFormView.as_view(), name='edit-student-form'),
    path('delete_student/<int:pk>', DeleteStudentView.as_view(), name='delete-student'),
]
