from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from . import validate
from django.contrib import auth
from .models import Article, HomeWorkToDo, HomeWorkFiles, Student, Mark, HomeWorkToDoFiles, Classroom, HomeworkToReceive
from django.utils.safestring import mark_safe
import json

class RegisterView(View):
	def post(self, request):
		if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
			name = request.POST.get('name')
			email = request.POST.get('email')
			password = request.POST.get('password')
			password2 = request.POST.get('password2')
			std_ID = request.POST.get("UUID")
			responseText = validate.validate_input(name,email,password,password2)
			if (responseText == 'valid' and not User.objects.filter(username=name).exists() and not User.objects.filter(email = email).exists()):
				user = User.objects.create_user(username=name,email=email,password=password)
				user.save()
				
				student_created = Student.objects.create(name=name,email=email,user_student = user,student_id=std_ID)
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
			if request.POST.get("purpose") == "add_homework":
				title = request.POST.get("title")
				description = request.POST.get("description")
				grade = request.POST.get("grade")
				files = request.FILES.getlist("files")
				new_home = HomeWorkToDo.objects.create(title = title, description = description, grade = grade)
				for file in files:
					new_home.homework_files.add(HomeWorkFiles.objects.create(files = file))
				new_home.save()
				current_classroom = Classroom.objects.get(number = grade)
				for student in current_classroom.students.all():
					student.homework_to_do += 1
					student.save()
			elif request.POST.get("purpose") == "send_homework_to_teacher":
				files = request.FILES.getlist("files")
				current_std = Student.objects.get(user_student = request.user)
				current_std.homework_done += 1
				homeworkToRecv = HomeworkToReceive.objects.create(student_obj = request.user.student)
				for file in files:
					homeworkToRecv.hm_files.add(HomeWorkToDoFiles.objects.create(files = file))
					print(file)
				if current_std.homework_to_do > 0:
					current_std.homework_to_do -= 1
				current_std.save()
				homeworkToRecv.save()
		else:
			grade = request.POST.get("number-class-students")
			month = request.POST.get("number-month-students")
			all_students = Student.objects.filter(grade=grade)
			all_marks = []
			for std in all_students:
				for mark in std.marks.all():
					all_marks.append([mark.day,mark.month,mark.present,mark.number,std.student_id])

			context = {
				'students':zip(all_students,list(range(0,len(all_students)))),
				"range":list(range(1,32)),
				"month":month,
				"grade":grade,
				"range2":len(list(Student.objects.filter(grade=grade))),
				"marks":json.dumps(all_marks),
				"homeworks": HomeWorkToDo.objects.filter(grade=grade)
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
	def post(self, request):
		file = request.FILES.get("file-input-profile")
		current_student = Student.objects.get(user_student = request.user)
		current_student.image = file
		current_student.save()
		try:
			gpa = 0
			cnt = 0
			current_std = Student.objects.get(user_student = request.user)
			for mark in current_std.marks.all():
				gpa += int(mark.number)
				cnt += 1

			context = {
				"student":Student.objects.get(user_student = request.user),
				"gpa":float(gpa/cnt)
			}
		except:
			context = {}
		return render(request,'profile.html',context=context)

	def get(self, request):
		try:
			gpa = 0
			cnt = 0
			current_std = Student.objects.get(user_student = request.user)
			for mark in current_std.marks.all():
				gpa += int(mark.number)
				cnt += 1

			context = {
				"student":Student.objects.get(user_student = request.user),
				"gpa":float(gpa/cnt)
			}
		except:
			context = {}
		return render(request,'profile.html',context=context)
