from django.conf.urls import patterns, url

from locationlib import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^new/$', views.new, name='new'),
	url(r'^savenew/$', views.savenew, name='savenew'),
	url(r'^(?P<location_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<location_id>\d+)/edit/$', views.edit, name='edit'),
	url(r'^(?P<location_id>\d+)/save/$', views.save, name='save'),
	url(r'^(?P<location_id>\d+)/delete/$', views.delete, name='delete'),
	)