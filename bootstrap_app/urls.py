from django.conf.urls import *
from views import BootstrapView


urlpatterns = patterns('',

    url(r'^mainhtml/',
        BootstrapView.as_view(),
        name='bsa'),
)
