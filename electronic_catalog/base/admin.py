from django.contrib import admin
from .models import Student, Mark, Article, HomeWorkToDo, HomeWorkFiles

admin.site.register(HomeWorkFiles)
admin.site.register(HomeWorkToDo)
admin.site.register(Student)
admin.site.register(Article)
admin.site.register(Mark)