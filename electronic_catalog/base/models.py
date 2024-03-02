from django.db import models
import uuid

class Student(models.Model):
	grade = models.IntegerField(default = 0,blank = False,editable = True)
	gpa = models.FloatField(default = 0,blank = False,editable = True)
	name = models.CharField(max_length = 100,blank = False,editable = True)
	email = models.EmailField(max_length = 100,blank = False,editable = True)
	homework_to_do = models.IntegerField(default = 0,blank = False,editable = True)
	homework_done = models.IntegerField(default = 0,blank = False,editable = True)
	student_id = models.UUIDField(default = uuid.uuid4(),blank = False,editable=False)
	image = models.ImageField(upload_to = 'media',default = "user.png",blank = True, null = True)
	
class Mark(models.Model):
	number = models.IntegerField(default=0)
	month = models.CharField(max_length = 15,blank = False,editable = False)
	day = models.IntegerField(default = 0)
	present = models.BooleanField(default = False)
	student_obj = models.OneToOneField(Student,on_delete=models.CASCADE)

class Article(models.Model):
	title = models.CharField(max_length = 100,blank = False,editable = True,default = "Article")
	description = models.TextField(blank = False,editable = True)
	image = models.ImageField(upload_to = 'media',default = "user.png",blank = True, null = True)
	date_posted = models.DateField(auto_now_add = True)
	article_id = models.UUIDField(default = uuid.uuid4(),blank = False,editable=False)