from django.conf.urls import patterns, url, include
from django.contrib import admin
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'rango.views.home', name='home'),
#    url(r'^rango_app/', 'rango_app.views.rango_app_view', name='rango_app'),
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

