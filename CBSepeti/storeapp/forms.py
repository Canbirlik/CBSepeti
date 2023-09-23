from django import forms
from django.forms import ModelForm
from . import models

"""
class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label="Nickname", max_length=50)
    message_input = forms.CharField(label="Your Message", max_length=150,widget=forms.Textarea(attrs={"class":"tweetmessage"}))

class AddTweetModelForm(ModelForm):
    class Meta:
        model = models.Tweet
        fields = ["nickname","message"]

"""