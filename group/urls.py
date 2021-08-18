from django.urls import path

from .views import (
    create_group_form,
    delete_group,
    edit_group_form,
    list_groups,
)


urlpatterns = [
    path('list_groups/', list_groups, name='list-groups'),
    path('create_group_form/', create_group_form, name='create-group-form'),
    path('edit_group_form/<int:group_id>', edit_group_form, name='edit-group-form'),
    path('delete_group/<int:group_id>', delete_group, name='delete-group')

]
