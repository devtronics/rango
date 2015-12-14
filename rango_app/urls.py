from django.conf.urls import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from views import category


urlpatterns = patterns('',

#    url(r'^category/(?P<category_name_slug>\w+)/$',
#        views.category, name='category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        category,
        name='category'),

    url(r'^add_category/$', views.add_category, name='add_category'),


)
