from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import StudentSerializer, MarkSerializer, ArticleSerializer, HomeworkSerializer, HomeworkReceiveSerializer, ClassRoomSerializer
from base.models import Student, Mark, Article, HomeWorkToDo, HomeworkToReceive, Classroom

class ArticleDetail(generics.RetrieveAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'pk'


class ArticleCreate(generics.CreateAPIView):
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

class ArticleList(generics.ListAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class ArticleUpdate(generics.UpdateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'pk'

class ArticleDelete(generics.DestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	lookup_field = 'pk'

	def perform_delete(self, instance):
		print("Deleted Article")
		super().perform_delete(instance)