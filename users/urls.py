from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
	url(r'^(?P<user_id>\d+)/$' , views.profile, name='profile'),
	url(r'^(?P<user_id>\d+)/edit/$', views.edit, name='edit'),
	url(r'^(?P<user_id>\d+)/places/$', views.places_index, name='places'),
	#url(r'^(?P<user_id>\d+)/places/edit/$',views.places_edit, name='places_edit')
	)