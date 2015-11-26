# coding: utf-8
from django.conf.urls import patterns, url, include
import room.views as views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(
        regex=r'^room/create/$',
        view=login_required(views.RoomCreateView.as_view()),
        name='chat_room_create',
    ),
)
