from django import forms
from django.contrib import messages
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import fields, models, widgets
from .models import Student

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['address', 'email', 'username']  #'__all__'  #


        # widgets = {
        #     "address" : forms.TextInput(attrs={"class":"form-control"})
        # }


class sjhgdfhdsj(StudentForm):
    pass


class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] 
