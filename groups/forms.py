from django import forms
from django.core.exceptions import ValidationError

from .models import Group
from students.models import Student
from teachers.models import Teacher

"""
class GroupForm(forms.Form):
    group_name = forms.CharField(label='Group name:', required=True, max_length=40)
    discipline = forms.CharField(label='Discipline:', required=True, max_length=40)
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all())
    curator = forms.ModelChoiceField(queryset=Teacher.objects.all())"""


class GroupFormFormModel(forms.ModelForm):
    def clean_students(self):
        students = self.cleaned_data['students']
        if len(students) > 10:
            raise forms.ValidationError('You can add maximum 10 students')
        return students

    class Meta:
        model = Group
        fields = ['group_name', 'discipline', 'curator', 'headman', 'students']
        widgets = {
            'students': forms.CheckboxSelectMultiple()
        }
