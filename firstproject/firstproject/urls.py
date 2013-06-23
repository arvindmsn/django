from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/$', 'firstproject.views.login_page',
	  name="login"),
    url(r'^questions/$', 'sample.views.index',
	  name="questions"),
    url(r'^$', 'firstproject.views.homepage', 
	  name="homepage"),
    url(r'^questions/(?P<question_id>\d+)/$', 
	  'sample.views.question_detail',
	  name='question_detail'),
    url(r'^questions/create/$',
	  'sample.views.question_create',
	  name="question_create"),
    url(r'^questions/edit/(?P<question_id>\d+)/$',
	  'sample.views.question_edit',
	  name='question_edit'),
    url(r'^logout/$', 'firstproject.views.logout_view',
	  name="logout"),
    # Examples:
    # url(r'^$', 'firstproject.views.home', name='home'),
    # url(r'^firstproject/', include('firstproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
