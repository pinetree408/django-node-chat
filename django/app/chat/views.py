# coding: utf-8
from django.views.generic import ListView, CreateView, DeleteView
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

# chat model, from
from models import Room, Message
from forms import RoomForm

import json


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    template_name = "chat/room_create.html"
    success_url = "/"

    def form_valid(self, form):
        self.object = form.save()
        return super(RoomCreateView, self).form_valid(form)


class MessageListView(ListView):
    temaplate_name = "chat/message_list.html"

    def get_queryset(self):
        room = Room.objects.filter(name=self.kwargs['room_name'])[0]
        queryset = Message.objects.filter(room=room)
        return queryset

    def get_context_data(self, *args, **kwargs):
        room = Room.objects.filter(name=self.kwargs['room_name'])[0]
        context = super(MessageListView, self).get_context_data(*args, **kwargs)
        context['async_url'] = settings.ASYNC_BACKEND_URL
        context['room'] = room
        return context


class MessageCreateView(CreateView):
    model = Message
    template_name = "chat/message_create.html"
    success_url = reverse_lazy("chat_message_list")
    fields = "__all__"

    def form_valid(self, form):
        self.object = form.save()
        if self.request.is_ajax():
            context = {'status': 'ok', 'message': self.object.as_dict()}
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            return HttpResponseRedirect(self.get_success_url())


class MessageDeleteView(DeleteView):
    model = Message

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        if self.request.is_ajax():
            return HttpResponse(json.dumps({'status': 'ok'}), content_type="application/json")
        else:
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("chat_message_list")
