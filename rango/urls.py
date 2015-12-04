from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'rango.views.home', name='home'),
    url(r'^rango_app/$', include('rango_app.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
