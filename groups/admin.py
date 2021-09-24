from django.contrib import admin

from .models import Group


@admin.register(Group)
class GroutAdmin(admin.ModelAdmin):
    list_display = ("id", "group_name", "faculty_name", "number_of_students")
    list_filter = ("group_name", "faculty_name", "number_of_students")
    search_fields = ("group_name__startswith", "faculty_name__startswith", )
