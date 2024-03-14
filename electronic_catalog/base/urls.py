from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomeView.as_view(),name="home-page"),
    path("article/",views.ArticlesView.as_view(),name="article-page"),
   	path("login/",views.LoginView.as_view(),name="login-page"),
    path("register/",views.RegisterView.as_view(),name="register-page"),
    path("profile/",views.ProfileView.as_view(),name="profile-page"),
    path("logout/",views.logout_view,name="logout-page")
]
