# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'yu_demo.views',
    # (r'^$', 'home'),
    (r'^$', 'test1'),
    (r'^get_app_info/$', 'get_app_info'),

)
