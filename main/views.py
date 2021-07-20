from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main import apps

req = 0
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
			return HttpResponseRedirect('cities/')
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

def cities(request):
	global req
	req = apps.Request()
	return render(request, 'main/cities.html')

def signup(request):
	answer = '<h1>Signup</h1>'
	return HttpResponse(answer)

def reset(request):
	answer = '<h1>Reset</h1>'
	return HttpResponse(answer)

def detect(request):
	return render(request, 'main/detect.html')

@csrf_exempt
def player(request):
	global req
	message = request.POST.get('data')
	response = req.find_city(message,0)
	apps.talk(response)
	return JsonResponse({'data': response})

