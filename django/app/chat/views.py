# coding: utf-8
from django.views.generic import ListView, CreateView, DeleteView
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

# chat model
from chat import models

import json

class MessageListView(ListView):
    queryset = models.Message.objects.all()[:10]
    temaplate_name = "chat/message_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MessageListView, self).get_context_data(*args, **kwargs)
        context['async_url'] = settings.ASYNC_BACKEND_URL
        return context

class MessageCreateView(CreateView):
    model = models.Message
    fields = '__all__'
    template_name = "chat/message_create.html"
    success_url = reverse_lazy("chat_message_list")

    def form_valid(self, form):
        self.object = form.save()
        if self.request.is_ajax():
            context = {'status': 'ok', 'message': self.object.as_dict()}
            return HttpResponse(json.dumps(context), content_type="application/json")
        else:
            return HttpResponseRedirect(self.get_success_url())

class MessageDeleteView(DeleteView):
    model = models.Message

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        if self.request.is_ajax():
            return HttpResponse(json.dumps({'status': 'ok'}), content_type="application/json")
        else:
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
    	return reverse("chat_message_list")
