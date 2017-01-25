from django.conf.urls import url
from django.contrib import admin
from posts.views import (
        post_list,
        post_create,
        post_detail,
        post_update,
        post_delete,
        )

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<pk>[\w-]+)/delete/$', post_delete, name='delete'),
    url(r'^(?P<pk>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<pk>[\w-]+)/$', post_detail, name='detail'),

]
