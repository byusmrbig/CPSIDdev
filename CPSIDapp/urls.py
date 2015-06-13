from django.conf.urls import url, patterns, include
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^[0-9]+/index$',views.index, name='index'),
	url(r'^(?P<id>[0-9]+)/$', views.incidentDetail, name='incidentDetail'),
	url(r'^test$', views.test, name='index'),
]

