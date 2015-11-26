# coding: utf-8
from django import forms
from room import models


class RoomForm(forms.ModelForm):

    class Meta:
        model = models.Room
        fields = "__all__"
