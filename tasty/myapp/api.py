#from django.contrib.auth.models import User
#from tastypie import fields
from tastypie.resources import ModelResource
from myapp.models import Sample

#class UserResource(ModelResource):
#	class Meta:
#		queryset = User.objects.all()
#		resource_name = 'user'
		
class SampleResource(ModelResource):
#	user = fields.ForeignKey(UserResource, 'user')
	
	class Meta:
		queryset = Sample.objects.all()
		resource_name = 'sample'
		list_allowed_methods = ['get', 'post', 'put', 'delete']
		detailed_allowed_methods = ['get', 'post', 'put', 'delete']
