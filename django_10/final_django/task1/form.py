
from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, required=True, label='Введите логин')
    password = forms.CharField(max_length=8, required=True, label='Введите пароль')
    repeat_password = forms.CharField(max_length=8, required=True, label='Повторите пароль')
    age = forms.CharField(max_length=3, required=True, label='Введите свой возраст')
