from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Student

"""
class StudentForm(forms.Form):
    first_name = forms.CharField(label='Student first name', required=True, max_length=200)
    last_name = forms.CharField(label='Student last name', required=True, max_length=200)
    age = forms.IntegerField(label='Student age')
    phone = PhoneNumberField(label='Phone number')
"""


class StudentFormFormModel(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'phone']


class GenerateStudentForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(2),
            MaxValueValidator(500),
        ]
    )
