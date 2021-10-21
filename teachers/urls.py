from django.urls import path

from .views import (
    CreateTeacherFormView,
    DeleteTeacherView,
    EditTeacherFormView,
    GenerateTeacherView,
    GenerateTeachersView,
    ListTeachersView,

)


urlpatterns = [
    path('list_teachers/', ListTeachersView.as_view(), name='list-teachers'),
    path('generate-teacher/', GenerateTeacherView.as_view(), name='generate-teacher'),
    path('generate-teachers/', GenerateTeachersView.as_view(), name='generate-teachers'),
    path('create_teacher_form/', CreateTeacherFormView.as_view(), name='create-teacher-form'),
    path('edit_teacher_form/<int:pk>', EditTeacherFormView.as_view(), name='edit-teacher-form'),
    path('delete_teacher/<int:pk>', DeleteTeacherView.as_view(), name='delete-teacher'),
]
