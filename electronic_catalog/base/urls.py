from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home-page"),
    path("article/",views.article,name="article-page"),
   	path("login/",views.login,name="login-page"),
    path("register/",views.register,name="register-page"),
    path("profile/",views.profile,name="profile-page"),
]
