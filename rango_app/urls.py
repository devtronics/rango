from django.conf.urls import patterns, include, url
from rango_app.views import BootstrapView


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
