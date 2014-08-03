from django.conf.urls import patterns,include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pushpin.views.home', name='home'),
    url(r'^signup/$', 'pushpin.views.signup', name="signup"),
    url(r'^login/$', 'pushpin.views.userLogin', name="userLogin"),
    url(r'^newuser/$', 'pushpin.views.createUser', name='createUser'),
    url(r'^authenticator/$', 'pushpin.views.authenticator', name='authenticator'),
    url(r'^logout/$', 'pushpin.views.userLogout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^locationlib/', include('locationlib.urls', namespace="locationlib")),
    url(r'^users/', include('users.urls', namespace='users')),
    )