from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^payzippy/', 'pay.views.index', name='homepage'),
	url(r'^pay/', 'pay.views.payment', name='form'),
	url(r'^charging/', 'pay.views.charging', name='charge'),
	url(r'^thankyou/$', 'pay.views.thankyou', name='thankyou'),
    # Examples:
    # url(r'^$', 'payzippy.views.home', name='home'),
    # url(r'^payzippy/', include('payzippy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
