from django.contrib import admin
from .models import Student, Mark, Article


admin.site.register(Student)
admin.site.register(Article)
admin.site.register(Mark)