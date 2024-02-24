from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,'base/home.html')

def article(request):
	return render(request,'base/article.html')

def login(request):
	return render(request,'base/login.html')

def register(request):
	return render(request,'base/sign_up.html')

def profile(request):
	return render(request,'base/profile.html')