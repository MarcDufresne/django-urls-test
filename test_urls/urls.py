from django.conf.urls import patterns, include, url
from django.contrib import admin
from wow.api import test_load_url, test_load_as_template, test_redirect_url

urlpatterns = patterns('',

        url(r'^admin/', include(admin.site.urls)),
)

test_load_url(urlpatterns)
test_load_as_template(urlpatterns)
test_redirect_url(urlpatterns)
