from rest_framework.response import Response
from rest_framework import generics
from .serializers import StudentSerializer, MarkSerializer, ArticleSerializer, HomeworkSerializer, HomeworkReceiveSerializer, ClassRoomSerializer
from base.models import Student, Mark, Article, HomeWorkToDo, HomeworkToReceive, Classroom
from .permissions import IsStaffUserPermission, IsHomeworkReceiver, IsTeacherPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .mixins import AuthAndPermissionMixin
from . import client

class ArticleDetail(AuthAndPermissionMixin, generics.RetrieveAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'pk'

class ArticleCreate(AuthAndPermissionMixin, generics.CreateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

	def perform_create(self, serializer):
		title = serializer.validated_data.get("title")
		description = serializer.validated_data.get("description")
		image = serializer.validated_data.get("image")
		article_id = serializer.validated_data.get("article_id")
		if image is None:
			image = "user.png"
		Article.objects.create(title = title,description = description,image = image,article_id = article_id).save()

class ArticleList(AuthAndPermissionMixin, generics.ListAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class ArticleUpdate(AuthAndPermissionMixin, generics.UpdateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'pk'

class ArticleDelete(AuthAndPermissionMixin, generics.DestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'pk'

	def perform_delete(self, instance):
		print("Deleted Article")
		super().perform_delete(instance)


# Algolia Search


class SearchStudentView(generics.GenericAPIView):
	def get(self, request, *args, **kwargs):
		query = request.GET.get('name')
		grade = request.GET.get('grade')
		#user = request.user
		results = client.perform_search(query,grade=grade)
		return Response(results)


# --------------------------

class StudentList(AuthAndPermissionMixin, generics.ListAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class StudentDetail(AuthAndPermissionMixin, generics.RetrieveAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	lookup_field = 'student_id'

class HomeworkList(generics.ListAPIView):
	queryset = HomeWorkToDo.objects.all()
	serializer_class = HomeworkSerializer
	permission_classes = [IsAuthenticated]
	authentication_classes = [SessionAuthentication, TokenAuthentication]

class HomeworkDetail(generics.RetrieveAPIView):
	queryset = HomeWorkToDo.objects.all()
	serializer_class = HomeworkSerializer
	lookup_field = 'pk'
	permission_classes = [IsAuthenticated, IsHomeworkReceiver]
	authentication_classes = [SessionAuthentication, TokenAuthentication]

class HomeworkReceiveList(generics.ListAPIView):
	queryset = HomeworkToReceive.objects.all()
	serializer_class = HomeworkReceiveSerializer
	permission_classes = [IsAuthenticated, IsTeacherPermission]
	authentication_classes = [SessionAuthentication, TokenAuthentication]

class ClassroomList(generics.ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassRoomSerializer
	permission_classes = [IsAuthenticated, IsTeacherPermission]
	authentication_classes = [SessionAuthentication, TokenAuthentication]

class ClassroomDetail(generics.RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassRoomSerializer
	permission_classes = [IsAuthenticated, IsTeacherPermission]
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	lookup_field = 'number'