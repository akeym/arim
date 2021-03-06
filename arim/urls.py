from django.conf.urls import patterns, url
from django.http import HttpResponseRedirect

from .views import *


urlpatterns = patterns(
    '',
    url(r'^$', lambda _: HttpResponseRedirect('/terms')),
    url(r'^terms$', terms_view),
    url(r'^device$', device_view),
    url(r'^device_list$', device_list_view),
    url(r'^delete_device$', delete_device_view),
    url(r'^logout$', 'django_cas.views.logout', name="logout_view"),
    url(r'^login$', 'django_cas.views.login', name="login_view"),
)
