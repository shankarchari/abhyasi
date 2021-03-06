#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Gowri Shankar
# @Date:   2015-04-04 21:39:23
# @Last Modified by:   Gowri Shankar
# @Last Modified time: 2015-04-14 22:24:23
from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# ex: /abhyasis/5/
    url(r'^(?P<abhyasi_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /abhyasis/5/results/
    url(r'^(?P<abhyasi_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^new/$', views.abhyasi_new, name='abhyasi_new'),
    url(r'^abhyasis/(?P<pk>[0-9]+)/edit/$', views.abhyasi_edit, name='abhyasi_edit'),
    url(r'^abhyasis/(?P<pk>[0-9]+)/sitting/new/$', views.sitting_new, name='sitting_new'),
    
]