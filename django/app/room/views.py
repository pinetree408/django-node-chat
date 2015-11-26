# coding: utf-8
from django.views.generic import CreateView
from django.shortcuts import render

# room model, from
from models import Room
from forms import RoomForm


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = "room/room_create.html"
    success_url = "/"

    def form_valid(self, form):
        self.object = form.save()
        return super(RoomCreateView, self).form_valid(form)
