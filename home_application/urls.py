# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns('home_application.views',
    (r'^$', 'index'),

    # for esb test
    (r'^esb_test/$', 'esb_test'),

    # for index
    (r'^index/$', 'index'),

   # get saltapi token
   (r'^self_api/$', 'self_api'),

   # get_flask_api token
   (r'^get_flask_api/$', 'get_flask_api'),
                       # 服务器列表
    (r'^server_list/$', 'server_list'),

    # 删除主机
    (r'^delete_server/$', 'delete_server'),
)
