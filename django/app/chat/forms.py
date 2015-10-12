# coding: utf-8
from django import forms
from chat import models


class MessageForm(forms.ModelForm):

    class Meta:
        model = models.Message
        fields = "__all__"


class RoomForm(forms.ModelForm):

    class Meta:
        model = models.Room
        fields = "__all__"
