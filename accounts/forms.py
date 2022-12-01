from dataclasses import field
from pyexpat import model
from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    password2=forms.CharField(required=True,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model = CustomUser
        fields = ['photo','first_name','last_name','username','email','phone_number','password','password2']
        widgets = {
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone_number":forms.NumberInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control"}),
            "photo":forms.FileInput(attrs={"class":"form-control"}),
        }