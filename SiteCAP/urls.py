from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

from siteW import views 

urlpatterns = patterns('',
	url(r'^$', include('siteW.urls')),
	url(r'^index/', views.index),
	url(r'^plans/', views.plans),
	url(r'^cours/', views.cours),
	)
