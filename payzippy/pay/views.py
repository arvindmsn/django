import urllib
import urllib2
import random
import hashlib

url = 'https://www.payzippy.com/payment/api/charging/v1'

# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import Http404, HttpResponseRedirect
from pay.forms import PayForm
from django.template import RequestContext
from pay.models import User

def index(request):
	return render_to_response('payzippy.html')

def payment(request):
	form = PayForm()
	return render_to_response('pay/pay.html', {'form' : form}, context_instance=RequestContext(request))
	
def charging(request):
	if request.method == 'POST':
		form = PayForm(request.POST)
		if form.is_valid():
			tr = random.randint(100, 999)
			tr_i  = str(tr)
			tr_id = 'MT' + tr_i
			user = User(
				buyer_name=form.cleaned_data['name'],
				buyer_email_address=form.cleaned_data['email'],
				buyer_phone_no=form.cleaned_data['phone'])
			string = '|' + user.buyer_email_address + '|' + user.buyer_phone_no + '|http://localhost:8000/thankyou/|INR||SHA256|test_t116|payment|' + tr_id + '|CREDIT|100|SALE|REDIRECT|809209a4e9caeb6548f65d6e66956b'
			m = hashlib.sha256(string).hexdigest()
			values = {
				  'bank_name' : '',
			          'buyer_email_address' : user.buyer_email_address,
			          'buyer_phone_no' : user.buyer_phone_no,
			          'callback_url' : 'http://localhost:8000/thankyou/',
			          'currency' : 'INR',
			          'emi_months' : '',
			          'hash' : m,
			          'hash_method' : 'SHA256',
			          'merchant_id' : 'test_t116',
			          'merchant_key_id' : 'payment',
			          'merchant_transaction_id' : tr_id,
			          'payment_method' : 'CREDIT',
			          'transaction_amount' : '100',
			          'transaction_type' : 'SALE',
			          'ui_mode' : 'REDIRECT',
          			}
          		data = urllib.urlencode(values)
			full_url = url + '?' + data
			return HttpResponseRedirect(full_url)
		else :
			form = PayForm()
		return render_to_response('pay/pay.html', {'form' : form}, context_instance=RequestContext(request))

def thankyou(request):
	return HttpResponse('Thank you!')
