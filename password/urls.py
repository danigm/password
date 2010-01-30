from django.conf.urls.defaults import *

from django.contrib import admin

from siteapp.models import Site

import settings

admin.autodiscover()
admin.site.register(Site)

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'', include('siteapp.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
