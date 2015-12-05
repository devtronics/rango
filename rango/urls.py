from django.conf.urls import *
from django.contrib import admin
from rango import views

urlpatterns = patterns('',
    # Examples:
    url(r'^rango/', 'rango.views.home', name='home'),
    url(r'^rango_app/$', include('rango_app.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^about', 'rango.views.about', name='about'),
    url(r'^contact', 'rango.views.contact', name='contact'),
)
