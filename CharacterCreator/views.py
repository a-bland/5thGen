from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

def home(request):
	return render(request, 'home.html')

def creation(request):
	return render(request, 'creation.html')

def battle(request):
	return render(request, 'battle.html')

def testcall(request):
	return HttpResponse(request.POST['text'])