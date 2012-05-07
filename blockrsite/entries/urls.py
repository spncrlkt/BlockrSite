from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^home/', 'entries.views.home'),
    url(r'^settings/', 'entries.views.administration'),
    url(r'^write/', 'entries.views.write'),
    url(r'^entries/', 'entries.views.list'),                       
)
