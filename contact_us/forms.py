from django import forms

from .models import ContactUs


class ContactUsFormFormModel(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title', 'message', 'email_from']