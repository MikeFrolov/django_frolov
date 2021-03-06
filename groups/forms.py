from django import forms

from .models import Group

"""
class GroupForm(forms.Form):
    group_name = forms.CharField(label='Group name:', required=True, max_length=40)
    discipline = forms.CharField(label='Discipline:', required=True, max_length=40)
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.all())
    curator = forms.ModelChoiceField(queryset=Teacher.objects.all())"""


class GroupFormFormModel(forms.ModelForm):
    def clean_students(self):
        students = self.cleaned_data['students']
        headman = self.cleaned_data['headman']
        if len(students) > 10:
            raise forms.ValidationError('You can add maximum 10 students!')
        elif headman not in students:
            raise forms.ValidationError('The headman must be in the group!')
        return students

    class Meta:
        model = Group
        fields = ['group_name', 'discipline', 'curator', 'headman', 'students']
        widgets = {
            'students': forms.CheckboxSelectMultiple()
        }
