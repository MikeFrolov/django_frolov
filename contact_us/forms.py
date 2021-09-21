from django import forms


class ContactUsForm(forms.Form):
    title = forms.CharField(label='Title:', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Message:', max_length=200,
                              widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))
    email_from = forms.CharField(label='Email from:', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __str__(self):
        return self.title, self.message, self.email_from
