from rango_app import views
from rango import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^rango_app_url/',
        'rango_app.views.rango_app_view',
        name='rango_app_view'),

    url(r'^bootstrap/',
        BootstrapView.as_view(),
        name='bootstrap_view'),

    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        'rango_app.views.category',
        name='category'),



)
