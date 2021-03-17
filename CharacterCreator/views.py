from django.shortcuts import render
from django.http import Http404

def home(request):
	return render(request, 'home.html')

def creation(request):
	return render(request, 'creation.html')

def battle(request):
	return render(request, 'battle.html')