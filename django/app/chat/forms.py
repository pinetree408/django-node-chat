# coding: utf-8
from django import forms
from chat import models


class MessageForm(forms.ModelForm):

    class Meta:
        model = models.Message
        fields = "__all__"
