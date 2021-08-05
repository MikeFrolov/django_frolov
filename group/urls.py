from django.urls import path

from . import views


urlpatterns = [
    path('create_group_form/', views.create_group_form),
    path('list_groups/', views.list_groups),
]
