from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mchacks.views.home', name='home'),
    # url(r'^mchacks/', include('mchacks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^move/(?P<col>\d+)/(?P<player>\d+)/', 'connect.views.place_move', name='place_move'),
    url(r'^reset/', 'connect.views.reset_game', name='reset_game'),
    url(r'^board/', 'connect.views.get_board', name='get_board'),
)
