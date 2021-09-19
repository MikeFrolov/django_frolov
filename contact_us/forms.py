from django import forms

from .models import ContactUs


class StudentFormFormModel(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title', 'message', 'email_from']