from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rango import views

urlpatterns = patterns('',
    url(r'^$', 'rango.views.home', name='home'),
# this is your problem    url(r'^rango_app/', 'rango_app.views.rango_app_view', name='rango_app'),
    url(r'^rango_app/', include('rango_app.urls'), name='rango_app'),
    url(r'^bsa/', include('bootstrap_app.urls'), name='bootstrap_app'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^media/(?P<path>,*)',
    'serve',
    {'document_root': settings.MEDIA_ROOT}), )

