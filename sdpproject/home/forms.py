from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email','password1']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = info_request
        fields = "__all__"

class DonateForm(forms.ModelForm):
    class Meta:
        model = donate
        fields = "__all__"
