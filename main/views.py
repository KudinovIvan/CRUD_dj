from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

def index(request):
	return render(request,'main/index.html')

def app(request):
	name = request.GET.get('name', 'none')
	return HttpResponse('<h1>App<h1><h3>{0}<h3>'.format(name))

def auth(request, id, name):
	answer = '<h1>User</h1><h3>id: {0} name: {1}</h3>'.format(id, name)
	return HttpResponse(answer)

def red(request):
	return HttpResponseRedirect('/app?name=REDIRECT')

def perm(request):
	return HttpResponsePermanentRedirect('/app?name=PERMANENT')
