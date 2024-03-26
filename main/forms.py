from django import forms
from django.forms import ModelForm, TextInput
from django_recaptcha.fields import ReCaptchaField
from django.contrib.auth.forms import UserCreationForm
from .models import SuperModel, News
from django.contrib.auth.models import User

class SuperModelForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = News
        fields = "__all__"



class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")