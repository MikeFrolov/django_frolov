from django.urls import path

from .views import (
    create_group_form,
    list_groups,
)


urlpatterns = [
    path('create_group_form/', create_group_form, name='create-group-form'),
    path('list_groups/', list_groups, name='list-groups'),
]
