from rest_framework import serializers
from base.models import Student, Mark, Article, HomeWorkToDo, HomeworkToReceive, Classroom

class UserSerializer(serializers.Serializer):
	username = serializers.CharField(read_only = True)
	email = serializers.CharField(read_only = True)


class MarkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mark
		fields = [
			'number',
			'month',
			'day',
			'present'
		]


class StudentSerializer(serializers.ModelSerializer):
	user_student = UserSerializer(read_only = True)
	student_image = serializers.SerializerMethodField(read_only = True)
	student_gpa = serializers.SerializerMethodField(read_only = True)
	marks = MarkSerializer(read_only = True, many = True)
	std_url = serializers.HyperlinkedIdentityField(view_name = 'student-detail',lookup_field = 'student_id')
	class Meta:
		model = Student
		fields = [
			'std_url',
			'grade',
			'student_gpa',
			'name',
			'email',
			'homework_to_do',
			'homework_done',
			'student_id',
			'student_image',
			'user_student',
			'marks',
		]


	def get_student_image(self, obj):
		return obj.image.url

	def get_student_gpa(self, obj):
		try:
			count = 0
			total = 0
			for mark in obj.marks.all():
				if mark != 0:
					count += 1
					total += mark.number

			return total/count
		except:
			return 0


class ArticleSerializer(serializers.ModelSerializer):
	detail_url = serializers.HyperlinkedIdentityField(
		view_name='article-detail',
		lookup_field='pk'
	)

	class Meta:
		model = Article

		fields = [
			'title',
			'description',
			'image',
			'date_posted',
			'article_id',
			'detail_url'
		]


class HomeworkReceiveSerializer(serializers.ModelSerializer):
	student_obj = StudentSerializer(read_only = True)
	hm_files = serializers.SerializerMethodField(read_only = True)
	class Meta:
		model = HomeworkToReceive
		fields = [
			'student_obj',
			'hm_files'
		]

	def get_hm_files(self, obj):
		urls = []

		for file in obj.hm_files.all():
			urls.append(file.files.path)
		return urls


class HomeworkSerializer(serializers.ModelSerializer):
	received_homework = HomeworkReceiveSerializer(many = True)
	homework_files = serializers.SerializerMethodField(read_only = True)
	students_that_send = StudentSerializer(many = True)
	class Meta:
		model = HomeWorkToDo
		fields = [
			'title',
			'pk',
			'description',
			'received_homework',
			'homework_id',
			'grade',
			'homework_files',
			'students_that_send'
		]

	def get_homework_files(self, obj):
		urls = []

		for file in obj.homework_files.all():
			urls.append(file.files.path)
		return urls

class ClassRoomSerializer(serializers.ModelSerializer):
	students = StudentSerializer(read_only = True,many = True)
	class Meta:
		model = Classroom

		fields = [
			'number',
			'students'
		]