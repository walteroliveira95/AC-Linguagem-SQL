from django.contrib.auth.forms import UserCreationForm
from core.models import User
from django import forms
from django.core.exceptions import ValidationError

class UserCreationForm(forms.Form):

    login = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['login'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("login already exists")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['login'],
            self.cleaned_data['password']
        )
        
        return user