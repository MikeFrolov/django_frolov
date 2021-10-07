from django.urls import path

from .views import (
    CreateGroupFormView,
    DeleteGroupView,
    EditGroupFormView,
    GroupsListView,
)


urlpatterns = [
    path('list_groups/', GroupsListView.as_view(), name='list-groups'),
    path('create_group_form/', CreateGroupFormView.as_view(), name='create-groups-form'),
    path('edit_group_form/<int:group_id>', EditGroupFormView.as_view(), name='edit-group-form'),
    path('delete_group/<int:pk>', DeleteGroupView.as_view(), name='delete-group')

]
