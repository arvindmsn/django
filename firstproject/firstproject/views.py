from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from firstproject.forms import LoginForm
from django.contrib.auth import authenticate, login, logout

def login_page(request):
	message = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					message = "you logged in with success"
				else:
					message = "your user is inactive"
			else:
				message = "invalid username and/or password"
	else:
		form = LoginForm()
	return render_to_response('login.html', {'message': message, 'form': form},
					context_instance=RequestContext(request))

def homepage(request):
	return render_to_response('homepage.html',
		context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return redirect('homepage')
