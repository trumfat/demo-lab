from django.conf.urls import patterns, include, url
from mysite.demo_lab import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
# test
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.avi),
	url(r'^update/$', views.update),
	url(r'^subscribe/$', views.subscribe),
	url(r'^hello/$', views.hello),
	url(r'^api/avi-version/$', views.avi_version),
	url(r'^api/avi-health/$', views.avi_health),
)
