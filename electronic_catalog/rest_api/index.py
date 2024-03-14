from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from base.models import Student

@register(Student)
class StudentIndex(AlgoliaIndex):
	fields = [
		'grade',
		'name',
		'email',
		'homework_to_do',
		'homework_done',
		'student_id',
		'user_student'
	]

	settings = {
		'searchableAttributes': ['name','email'],
		'attributesForFaceting': ['grade','user_student']
	}