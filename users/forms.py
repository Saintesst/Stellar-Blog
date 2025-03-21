from django import forms
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm




User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'maxlength': '20'}),
        max_length=20
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'maxlength': '20'}),
        max_length=20
    )

    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

class UserSearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=100)
    
    
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}) 
    )