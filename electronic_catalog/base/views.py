from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,'home.html')

def article(request):
	return render(request,'article.html')

def login(request):
	return render(request,'login.html')

def register(request):
	return render(request,'sign_up.html')

def profile(request):
	return render(request,'profile.html')