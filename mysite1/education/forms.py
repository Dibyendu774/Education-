from captcha.fields import CaptchaField
from django.forms import Form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import user


class Captcha(Form):
    cp = CaptchaField()


class Register1(UserCreationForm):
    email = forms.EmailField(max_length=2000, help_text='Required')

    class meta:
        model = user
        fields = ('password', 'email', 'username')
