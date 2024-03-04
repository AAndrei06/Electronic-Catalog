from django.db import models
from django.contrib.auth.models import User
import uuid

	
class Mark(models.Model):
	number = models.IntegerField(default=0)
	month = models.CharField(max_length = 15,blank = False,editable = False)
	day = models.IntegerField(default = 0)
	present = models.BooleanField(default = False)

class Student(models.Model):
	grade = models.IntegerField(default = 0,blank = False,editable = True)
	gpa = models.FloatField(default = 0,blank = False,editable = True)
	name = models.CharField(max_length = 100,blank = False,editable = True)
	email = models.EmailField(max_length = 100,blank = False,editable = True)
	homework_to_do = models.IntegerField(default = 0,blank = False,editable = True)
	homework_done = models.IntegerField(default = 0,blank = False,editable = True)
	student_id = models.UUIDField(default = uuid.uuid4(),blank = False,editable=True)
	image = models.ImageField(upload_to = '',default = "user.png",blank = True, null = True)
	user_student = models.OneToOneField(User,on_delete=models.CASCADE)
	marks = models.ManyToManyField(Mark)

class Article(models.Model):
	title = models.CharField(max_length = 100,blank = False,editable = True,default = "Article")
	description = models.TextField(blank = False,editable = True)
	image = models.ImageField(upload_to = '',default = "user.png",blank = True, null = True)
	date_posted = models.DateField(auto_now_add = True)
	article_id = models.UUIDField(default = uuid.uuid4(),blank = False,editable=False)

class HomeWorkToDo(models.Model):
	title = models.CharField(max_length = 100,blank = False,editable = True, default="HomeWork")
	description = models.CharField(max_length = 1000,blank = False,editable = True, default="Description")
	received_homework = models.ManyToManyField(Student,blank = True,editable = True)
	homework_id = models.UUIDField(default = uuid.uuid4(),blank = False,editable=False)
	grade = models.IntegerField(default = 0,blank = False,editable=False)

class HomeWorkFiles(models.Model):
	homework = models.ForeignKey(HomeWorkToDo,on_delete=models.CASCADE)
	files = models.FileField(upload_to="media")

class Classroom(models.Model):
	number = models.IntegerField(default = 0,blank = False,editable = True)
	students = models.ManyToManyField(Student,blank = True,editable = True)