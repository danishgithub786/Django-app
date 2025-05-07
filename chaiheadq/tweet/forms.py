from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  

class TweetForms(forms.ModelForm):
    # this meta class is necessary
    class Meta:
        model=Tweet
        fields=['text','photo']

class UserRegisterationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2') # here built in table is used thats why we used tuple