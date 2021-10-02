from django.contrib import admin

from .models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "group_name", "discipline", "curator", "headman", "students_list")
    list_filter = ("group_name", "discipline", "curator", "headman")
    search_fields = ("group_name__startswith", "discipline__startswith")
