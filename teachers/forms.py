from django import forms

# from .models import Teacher


class TeacherForm(forms.Form):
    first_name = forms.CharField(label='Teacher first name', required=True, max_length=200)
    last_name = forms.CharField(label='Teacher last name', required=True, max_length=200)
    age = forms.IntegerField(label='Teacher age')


"""class TeacherFormFormModel(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'age']
"""