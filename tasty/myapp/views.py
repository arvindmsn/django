# Create your views here.

from django.http import HttpResponse
from myapp.models import Sample

def index(request):
	samples = Sample.objects.all()
	response_string = "Samples <br/>"
	response_string += '<br/>'.join(["id: %s, title: %s" % (s.id, s.title) for s in samples])
	return HttpResponse(response_string)
