from django.contrib import admin
from .models import Student, Mark, Article, HomeWorkToDo, HomeWorkFiles, Classroom, HomeWorkToDoFiles, HomeworkToReceive

admin.site.register(HomeWorkToDoFiles)
admin.site.register(HomeworkToReceive)
admin.site.register(Classroom)
admin.site.register(HomeWorkFiles)
admin.site.register(HomeWorkToDo)
admin.site.register(Student)
admin.site.register(Article)
admin.site.register(Mark)