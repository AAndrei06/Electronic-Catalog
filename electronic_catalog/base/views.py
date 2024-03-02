from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from . import validate
from django.contrib import auth
from .models import Article

class RegisterView(View):
	def post(self, request):
		if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
			name = request.POST.get('name')
			email = request.POST.get('email')
			password = request.POST.get('password')
			password2 = request.POST.get('password2')
			responseText = validate.validate_input(name,email,password,password2)
			if (responseText == 'valid' and not User.objects.filter(username=name).exists() and not User.objects.filter(email = email).exists()):
				user = User.objects.create_user(username=name,email=email,password=password)
				user.save()
				userCreated = auth.authenticate(username=name, password=password)
				auth.login(request,user)
			return JsonResponse({"text":responseText},status = 200)
				
		return render(request,'sign_up.html')

	def get(self, request):
		return render(request,'sign_up.html')


class LoginView(View):
	def post(self, request):
		if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
			name = request.POST.get('name')
			password = request.POST.get('password')
			user = auth.authenticate(username=name, password=password)
			if user is not None:
			    auth.login(request,user)
			    return JsonResponse({"text":"valid"},status = 200)
			else:
				 return JsonResponse({"text":"User doesn't exist"},status = 200)
				
		return render(request,'login.html')

	def get(self, request):
		return render(request,'login.html')


class HomeView(LoginRequiredMixin, View):
	login_url = "/login/"
	redirect_field_name = "/"
	def get(self, request):
		return render(request,'home.html')

def logout_view(request):
	auth.logout(request)
	return redirect('login-page')

class ArticlesView(LoginRequiredMixin, View):
	login_url = "/login/"
	redirect_field_name = "article/"
	def get(self, request):
		context = {
			"articles":Article.objects.all().order_by('-date_posted')
		}
		return render(request,'article.html',context=context)


def profile(request):
	return render(request,'profile.html')