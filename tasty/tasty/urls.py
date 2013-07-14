from django.conf.urls.defaults import *
#from tastypie.api import Api
#from myapp.api import EntryResource, UserResource
from myapp.api import SampleResource

#v1_api = Api(api_name='v1')
#v1_api.register(UserResource())
#v1_api.register(EntryResource())

sample_resource = SampleResource()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^samples/$', 'myapp.views.index'),
    # Examples:
    # url(r'^$', 'tasty.views.home', name='home'),
    # url(r'^tasty/', include('tasty.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #(r'^blog/', include('myapp.urls')),
    #url(r'^api/', include(v1_api.urls)),
    url(r'^api/', include(sample_resource.urls)),
)
