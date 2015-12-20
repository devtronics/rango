from django.conf.urls import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rango_app.views import category


urlpatterns = patterns('',

#    url(r'^category/(?P<category_name_slug>\w+)/$',
#        views.category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
       'rango_app.views.category',
        name='category'),

    url(r'^add_category/$',
       'rango_app.views.add_category',
        name='add_category'),

    url(r'^add_page/$',
        'rango_app.views.add_page',
        name='add_page'),
)
