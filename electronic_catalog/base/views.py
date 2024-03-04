from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from . import validate
from django.contrib import auth
from .models import Article, HomeWorkToDo, HomeWorkFiles, Student, Mark

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
				
				student_created = Student.objects.create(name=name,email=email,user_student = user)
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
	def post(self, request):
		context = {}
		if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
			title = request.POST.get("title")
			description = request.POST.get("description")
			grade = request.POST.get("grade")
			files = request.FILES.getlist("files")
			print(title)
			print(description)
			print(grade)
			new_home = HomeWorkToDo.objects.create(title = title, description = description, grade = grade)
			for file in files:
				HomeWorkFiles.objects.create(files = file,homework = new_home).save()
		else:
			grade = request.POST.get("number-class-students")
			month = request.POST.get("number-month-students")
			print(grade)
			print(month)
			context = {
				'students':Student.objects.filter(grade=grade),
				"range":list(range(1,32)),
				"month":month,
				"grade":grade,
				"range2":len(list(Student.objects.filter(grade=grade)))
			}

		return render(request,'home.html',context)

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


class ProfileView(LoginRequiredMixin, View):
	login_url = "/login/"
	redirect_field_name = "profile/"
	def get(self, request):
		try:
			context = {
				"student":Student.objects.get(user_student = request.user),
			}
		except:
			context = {}
		return render(request,'profile.html',context=context)


def profile(request):
	return render(request,'profile.html')