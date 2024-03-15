from celery import shared_task
from .models import Article, HomeWorkToDo, HomeWorkFiles, Classroom, Student, Mark, HomeworkToReceive, HomeWorkToDoFiles
from rest_framework.authtoken.models import Token


@shared_task(serializer="pickle")
def create_homework(title, description, grade, files):
	new_home = HomeWorkToDo.objects.create(title = title, description = description, grade = grade)
	for file in files:
		new_home.homework_files.add(HomeWorkFiles.objects.create(files = file))
	new_home.save()
	current_classroom = Classroom.objects.get(number = grade)
	for student in current_classroom.students.all():
		student.homework_to_do += 1
		student.save()

@shared_task
def student_to_class(student_id, classroom):
	class_of_std = Classroom.objects.get(number = classroom)
	student_obj = Student.objects.get(student_id=student_id)
	student_obj.grade = classroom
	student_obj.save()
	class_of_std.students.add(student_obj)

@shared_task
def rm_student_from_class(student_id):
	student_obj = Student.objects.get(student_id=student_id)
	classroom = Classroom.objects.get(number = student_obj.grade)
	classroom.students.remove(student_obj)
	student_obj.grade = 0
	student_obj.save()

@shared_task
def add_mark(month, day, studentID, mark):
	student = Student.objects.get(student_id = studentID)
	if (int(mark) == 99999):
		student.marks.filter(day = day, month = month).delete()
	else:
		markStd = None
		present = False
		if int(mark) > 0:
			present = True
		else:
			present = False
		if (student.marks.filter(day = day, month = month).exists()):
			student.marks.filter(day = day, month = month).delete()
		
		markStd = Mark.objects.create(number = mark,month = month,day=day,present=present)
		student.marks.add(markStd)

@shared_task(serializer="pickle")
def send_homework(files, pk, user):
	current_std = Student.objects.get(user_student = user)
	current_std.homework_done += 1
	homeworkDone = HomeWorkToDo.objects.get(id = pk)
	homeworkDone.students_that_send.add(user.student)
	homeworkDone.save()
	homeworkToRecv = HomeworkToReceive.objects.create(student_obj = user.student)
	for file in files:
		homeworkToRecv.hm_files.add(HomeWorkToDoFiles.objects.create(files = file))
	if current_std.homework_to_do > 0:
		current_std.homework_to_do -= 1
	current_std.save()
	homeworkToRecv.save()

@shared_task
def delete_auth():
	for token in Token.objects.all():
		token.delete()