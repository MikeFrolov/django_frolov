from django.contrib import admin
from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("sent_date", "title", "email_from")
    list_filter = ("sent_date", "email_from")
    search_fields = ("sent_date__startswith", "email_from__startswith")
