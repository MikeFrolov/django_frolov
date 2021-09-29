from django.contrib import admin

from .models import Exchange


@admin.register(Exchange)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("create_at", "source", "currency", "buy_price", "sale_price")
    list_filter = ("currency", "source")
    search_fields = ("source__startswith", "currency__startswith")
