from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class UserSearchForm(forms.Form):
    query = forms.CharField(label="Поиск пользователя", max_length=100)