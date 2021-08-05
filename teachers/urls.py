from django.urls import path

from . import views


urlpatterns = [
    path('create_teacher_form/', views.create_teacher_form),
    path('list_teachers/', views.list_filtered_teachers),
]
