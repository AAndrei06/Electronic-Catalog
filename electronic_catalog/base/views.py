from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User
from . import validate

class RegisterView(View):
	def post(self, request):
		if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
			name = request.POST.get('name')
			email = request.POST.get('email')
			password = request.POST.get('password')
			password2 = request.POST.get('password2')
			print(name)
			print(email)
			print(password)
			print(password2)

			if (validate.validate_input(name,email,password,password2) == 'valid' and not User.objects.filter(username=name).exists() and not User.objects.filter(email = email).exists()):
				print("success")
				user = User.objects.create_user(username=name,email=email,password=password)
				user.save()
				return JsonResponse({"text":"Created"},status = 200)
			else:
				print(validate.validate_input(name,email,password,password2))
				return JsonResponse({"text":"Not good"},status = 200)

		return render(request,'sign_up.html')

	def get(self, request):
		return render(request,'sign_up.html')



def home(request):
	return render(request,'home.html')

def article(request):
	return render(request,'article.html')

def login(request):
	return render(request,'login.html')


def profile(request):
	return render(request,'profile.html')