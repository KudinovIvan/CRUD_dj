from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
	type_of = request.GET.get('action', 'none')
	login = request.GET.get('login', 'none')
	password = request.GET.get('password', 'none')
	repass = request.GET.get('repass', 'none')
	mail = request.GET.get('mail', 'none')
	mail = mail.replace('%40', '@')
	if (type_of == 'signin'):
		user = authenticate(username=login, password=password) 
		if user is not None:
			return HttpResponseRedirect('signin/')
		else:
			return HttpResponseRedirect('/?error=#error_signin')
	elif (type_of == 'signup'):
		user = authenticate(username=login, password=password)
		if user is not None:
			return HttpResponseRedirect('/?error=#error_signup')
		else:
			if (repass == password):
				user = User.objects.create_user(login, mail, password)
				return HttpResponseRedirect('/?success=#success_up')
			else:
				return HttpResponseRedirect('?error=#error_signup_password')
	elif (type_of == 'reset'):
		user = User.objects.get(username=login)
		if user is not None:
			return HttpResponseRedirect('reset/')
		else:
			return HttpResponseRedirect('/?error=#error_reset')
	return render(request,'main/index.html')

def app(request):
	name = request.GET.get('name', 'none')
	return HttpResponse('<h1>App<h1><h3>{0}<h3>'.format(name))

def signin(request):
	answer = '<h1>Signin</h1>'
	return HttpResponse(answer)

def signup(request):
	answer = '<h1>Signup</h1>'
	return HttpResponse(answer)

def reset(request):
	answer = '<h1>Reset</h1>'
	return HttpResponse(answer)

def red(request):
	return HttpResponseRedirect('/app?name=REDIRECT')

def perm(request):
	return HttpResponsePermanentRedirect('/app?name=PERMANENT')