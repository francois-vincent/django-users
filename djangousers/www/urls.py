# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url, include
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'www.common.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^common/', include('www.common.urls', namespace='common')),
    url(r'^users/', include('www.users.urls', namespace='users')),
)
