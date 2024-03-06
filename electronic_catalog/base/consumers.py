import json
import base64
from .models import Article, Classroom, Student, Mark
from django.core.files.base import ContentFile
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async

@database_sync_to_async
def create_report(title,desc,image):
	return Article.objects.create(title=title,description=desc,image=image)

@database_sync_to_async
def edit_report(title,desc,article_id):
	article = Article.objects.get(article_id=article_id)
	article.description = desc
	article.title = title
	article.save()

@database_sync_to_async
def delete_report(article_id):
	return Article.objects.get(article_id=article_id).delete()

@database_sync_to_async
def add_student_to_classroom(student_id, classroom):
	class_of_std = Classroom.objects.get(number = classroom)
	student_obj = Student.objects.get(student_id=student_id)
	student_obj.grade = classroom
	student_obj.save()
	class_of_std.students.add(student_obj)

@database_sync_to_async
def remove_student_from_classroom(student_id):
	student_obj = Student.objects.get(student_id=student_id)
	classroom = Classroom.objects.get(number = student_obj.grade)
	classroom.students.remove(student_obj)
	student_obj.grade = 0
	student_obj.save()

@database_sync_to_async
def add_mark_to_student(month, day, studentID, mark):
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
	

class CatalogConsumer(AsyncWebsocketConsumer):

	async def connect(self):
		self.room_group_name = "home"
		await self.channel_layer.group_add(self.room_group_name, self.channel_name)
		await self.accept()

	async def disconnect(self, close_code):
		await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json["message"]
		if (message == "Article Create"):
			title = text_data_json["title"]
			desc = text_data_json["description"]
			image = text_data_json["image"]
			format, imgstr = image.split(';base64,') 
			ext = format.split('/')[-1] 
			data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
			await create_report(title,desc,data)

		elif (message == "Article Edit"):
			await edit_report(text_data_json["title"],text_data_json["description"],text_data_json["id"])
			await self.channel_layer.group_send(self.room_group_name, {"type": "chat.message",
																	   "message": message,
																	   "id":text_data_json["id"],
																	   "title":text_data_json["title"],
																	   "description":text_data_json["description"]})
		elif (message == "Article Delete"):
			await delete_report(text_data_json["id"])
			await self.channel_layer.group_send(self.room_group_name, {"type": "chat.message",
																	   "message": message,
																	   "id":text_data_json["id"]})
		elif (message == "Student Add"):
			await add_student_to_classroom(text_data_json["ID"],text_data_json["classroom"])
			await self.channel_layer.group_send(self.room_group_name, {"type": "chat.message",
																	   "message": message})
		elif (message == "Student Remove"):
			await remove_student_from_classroom(text_data_json["ID"])
			await self.channel_layer.group_send(self.room_group_name, {"type": "chat.message",
																	   "message": message})
		elif (message == "Add Mark"):
			await add_mark_to_student(text_data_json["month"],text_data_json["day"],text_data_json["student_id"],text_data_json["mark"])
			await self.channel_layer.group_send(self.room_group_name,{"type":"chat.message",
																      "message":message,
																	  "day":text_data_json["day"],
																	  "month":text_data_json["month"],
																	  "student_id":text_data_json["student_id"],
																	  "mark":text_data_json["mark"],
																	  "present":int(text_data_json["mark"]) > 0})
		else:
			await self.channel_layer.group_send(self.room_group_name, {"type": "chat.message",
																	   "message": message})

	async def chat_message(self, event):
		message = event["message"]
		if (message == "Article Edit"):
			await self.send(text_data=json.dumps({"message":message,
												  "id":event["id"],
												  "title":event["title"],
												  "description":event["description"]}))
		elif(message == "Article Delete"):
			await self.send(text_data=json.dumps({"message":message,
												  "id":event["id"]}))
		elif (message == "Student Add" or message == "Student Delete"):
			await self.send(text_data=json.dumps({"message":message}))
		elif (message == "Add Mark"):
			await self.send(text_data = json.dumps({"message":message,
													"day":event["day"],
													"month":event["month"],
													"student_id":event["student_id"],
													"mark":event["mark"],
													"present":int(event["mark"]) > 0}))
		else:
			await self.send(text_data=json.dumps({"message":message}))