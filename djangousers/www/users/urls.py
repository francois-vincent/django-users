# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('www.users.views',
    url(r'^login/$', views.login_post, name='login'),
    url(r'^login_required/$', views.login_view, name='login_required'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^create_account/$', views.create_account, name='create_account'),
    url(r'^edit_account/$', views.edit_account, name='edit_account'),
    url(r'^change_password/$', views.change_password, name='change_password'),
)
