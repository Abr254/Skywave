# forms.py

from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

class MediaForm(forms.Form):
    media = forms.FileField()