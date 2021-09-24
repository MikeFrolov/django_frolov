from django.contrib import admin

from .models import Group


@admin.register(Group)
class GroutAdmin(admin.ModelAdmin):
    list_display = ("id", "group_name", "discipline")
    list_filter = ("group_name", "discipline")
    search_fields = ("group_name__startswith", "discipline__startswith")
