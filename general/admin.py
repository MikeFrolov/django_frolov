from django.contrib import admin

# Register your models here.

from .models import Logger


@admin.register(Logger)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('method', 'path', 'created', 'execution_time')
    list_filter = ('path', 'method')
