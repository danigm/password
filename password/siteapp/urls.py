from django.conf.urls.defaults import *

urlpatterns = patterns('siteapp.views',
    (r'^$', 'index'),
    (r'^submit/$', 'submit'),
    (r'^search/(?P<q>.*).json$', 'jsonsearch'),
    (r'^search/(?P<q>.*)$', 'search'),
    (r'^vote/(?P<id>\d+)/(?P<vote>1|0)$', 'vote'),
    (r'^vote/(?P<id>\d+)/(?P<vote>1|0).json$', 'jsonvote'),
)
