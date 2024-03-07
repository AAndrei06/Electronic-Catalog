from django.db import models
from django.contrib.auth.models import User
import uuid

	
class Mark(models.Model):
	number = models.IntegerField(default=0)
	month = models.CharField(max_length = 15,blank = False)
	day = models.IntegerField(default = 0)
	present = models.BooleanField(default = False)

class Student(models.Model):
	grade = models.IntegerField(default = 0,blank = False)
	gpa = models.FloatField(default = 0,blank = False)
	name = models.CharField(max_length = 100,blank = False)
	email = models.EmailField(max_length = 100,blank = False)
	homework_to_do = models.IntegerField(default = 0,blank = False)
	homework_done = models.IntegerField(default = 0,blank = False)
	student_id = models.CharField(max_length=64,blank = False)
	image = models.ImageField(upload_to = '',default = "user.png",blank = True, null = True)
	user_student = models.OneToOneField(User,on_delete=models.CASCADE)
	marks = models.ManyToManyField(Mark,blank=True,null=True)

class Article(models.Model):
	title = models.CharField(max_length = 100,blank = False,default = "Article")
	description = models.TextField(blank = False)
	image = models.ImageField(upload_to = '',default = "user.png",blank = True, null = True)
	date_posted = models.DateField(auto_now_add = True)
	article_id = models.UUIDField(default = uuid.uuid4(),blank = False,editable=False)

class HomeWorkFiles(models.Model):
	files = models.FileField(upload_to='')

class HomeWorkToDoFiles(models.Model):
	files = models.FileField(upload_to = '')

class HomeworkToReceive(models.Model):
	student_obj = models.ForeignKey(Student,on_delete = models.CASCADE)
	hm_files = models.ManyToManyField(HomeWorkToDoFiles,blank = True,null = True)

class HomeWorkToDo(models.Model):
	title = models.CharField(max_length = 100,blank = False, default="Homework")
	description = models.CharField(max_length = 1000,blank = False, default="Description")
	received_homework = models.ManyToManyField(HomeworkToReceive,blank = True)
	homework_id = models.UUIDField(default = uuid.uuid4(),blank = False,editable=False)
	grade = models.IntegerField(default = 0,blank = False,editable=False)
	homework_files = models.ManyToManyField(HomeWorkFiles,blank = True,null = True)

class Classroom(models.Model):
	number = models.IntegerField(default = 0,blank = False)
	students = models.ManyToManyField(Student,blank = True)