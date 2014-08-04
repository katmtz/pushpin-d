from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
	url(r'^(?P<user_id>\d+)/$' , views.profile, name='profile'),
	url(r'^(?P<user_id>\d+)/edit/$', views.edit, name='edit'),
	url(r'^(?P<user_id>\d+)/save/$', views.save, name='save'),
	url(r'^(?P<user_id>\d+)/places/$', views.places_index, name='places'),
	url(r'^(?P<user_id>\d+)/add/$', views.add, name='add'),
	)