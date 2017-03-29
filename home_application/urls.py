# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('home_application.views',
    (r'^$', 'index'),
    (r'^index/$', 'index'),

    # 服务器列表
    (r'^server_list/$', 'server_list'),

)
