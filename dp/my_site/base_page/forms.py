from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class Registration(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}))
    info = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'date_of_birth', 'info')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']