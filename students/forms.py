from django import forms

from .models import Student

"""
class StudentForm(forms.Form):
    first_name = forms.CharField(label='Student first name', required=True, max_length=200)
    last_name = forms.CharField(label='Student last name', required=True, max_length=200)
    age = forms.IntegerField(label='Student age')
"""


class StudentFormFormModel(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age']
