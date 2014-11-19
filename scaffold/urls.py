from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scaffold.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^_ah/', include('djangae.urls')),
    url(r'^$', 'legislativehistory.views.index'),
    url(r'^legislation/$', 'legislativehistory.views.legislation'),
    url(r'^(?P<state>[a-zA-Z]+)/(?P<session>[0-9|-]+)/$', 'legislativehistory.views.bill_detail'),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),
)
