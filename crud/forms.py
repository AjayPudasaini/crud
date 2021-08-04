from django import forms
from django.contrib import messages
from django.core import validators

class StudentForm(forms.Form):
    username = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class':'form-control', 'placceholder':'enter username'}))
    email = forms.EmailField(max_length=500, widget=forms.EmailInput(attrs={'class':'form-control', 'placceholder':'enter email address'}))
    address = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class':'form-control', 'placceholder':'enter address'}))

    def validation(self):
        username = self.cleaned_data['username']
        if username!='abc':
            raise forms.ValidationError("invalid username")
        return username