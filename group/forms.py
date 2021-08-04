from django import forms

from .models import Group

"""
class GroupForm(forms.Form):
    group_name = forms.CharField(label='Group name', required=True, max_length=200)
    faculty_name = forms.CharField(label='Faculty name', required=True, max_length=200)
    number_of_students = forms.IntegerField(label='Number of students')
"""


class GroupFormFormModel(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'faculty_name', 'number_of_students']
