from django import forms

from .models import Group

"""
class GroupForm(forms.Form):
    group_name = forms.CharField(label='Group name', required=True, max_length=40)
    discipline = forms.CharField(label='Discipline', required=True, max_length=40)
"""


class GroupFormFormModel(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'discipline']
