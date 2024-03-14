from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/',obtain_auth_token),
    path("article/<int:pk>/",views.ArticleDetail.as_view(),name="article-detail"),
    path("article/create/",views.ArticleCreate.as_view(),name="article-create"),
    path("article/",views.ArticleList.as_view(),name="article-list"),
    path("article/delete/<int:pk>/",views.ArticleDelete.as_view(),name="article-delete"),
    path("article/update/<int:pk>/",views.ArticleUpdate.as_view(),name="article-update"),
    path("student/",views.StudentList.as_view(),name="student-list"),
    path("student/<str:student_id>/",views.StudentDetail.as_view(),name="student-detail"),
    path("homework/",views.HomeworkList.as_view(),name="homework-list"),
    path("homework/<int:pk>/",views.HomeworkDetail.as_view(),name="homework-detail"),
    path("homework_receive/",views.HomeworkReceiveList.as_view(),name="homework-receive-list"),
    path("classroom/",views.ClassroomList.as_view(),name="classroom-list"),
    path("classroom/<int:number>/",views.ClassroomDetail.as_view(),name="classroom-detail"),
    path("student/list/search/",views.SearchStudentView.as_view(),name="search-student")
]
