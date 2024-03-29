import json
import base64
from .models import Article, Classroom, Student, Mark
from django.core.files.base import ContentFile
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from .tasks import student_to_class, rm_student_from_class, add_mark

@database_sync_to_async
def create_report(title,desc,image,uuid):
	return Article.objects.create(title=title,description=desc,image=image,article_id = uuid)

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
	student_to_class.delay(student_id, classroom)

@database_sync_to_async
def remove_student_from_classroom(student_id):
	rm_student_from_class.delay(student_id)

@database_sync_to_async
def add_mark_to_student(month, day, studentID, mark):
	add_mark.delay(month, day, studentID, mark)
	

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
			uuid = text_data_json["uuid"]
			format, imgstr = image.split(';base64,') 
			ext = format.split('/')[-1] 
			data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
			await create_report(title,desc,data,uuid)

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