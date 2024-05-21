from django import forms
from django.contrib.auth.forms import User
from encrypt_app.models import UserProfile


class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('teacher', 'profile_picture')
