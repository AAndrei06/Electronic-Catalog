from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("article/<int:pk>/",views.ArticleDetail.as_view(),name="article-detail"),
    path("article/create/",views.ArticleCreate.as_view(),name="article-create"),
    path("article/",views.ArticleList.as_view(),name="article-list"),
    path("article/delete/<int:pk>/",views.ArticleDelete.as_view(),name="article-delete"),
    path("article/update/<int:pk>/",views.ArticleUpdate.as_view(),name="article-update")
]
