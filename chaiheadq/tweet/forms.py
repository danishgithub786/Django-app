from django import forms
from .models import Tweet

class TweetForms(forms.ModelForm):
    # this meta class is necessary
    class Meta:
        model=Tweet
        fields=['text','photo']