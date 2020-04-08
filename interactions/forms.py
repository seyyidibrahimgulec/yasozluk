from django import forms
from django.shortcuts import redirect, render
from interactions.models import Message
from django.contrib.auth.models import User
from django.forms.widgets import Textarea


class NewMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text', 'send_to',)
        widgets = {
            'text': Textarea(attrs={'cols': 60, 'rows': 20}),
        }

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(NewMessageForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(NewMessageForm, self).save(commit=False)
        inst.send_by = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst
