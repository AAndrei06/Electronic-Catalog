import json
import base64
from .models import Article
from django.core.files.base import ContentFile
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async

@database_sync_to_async
def create_report(title,desc,image):
	print("Saved")
	return Article.objects.create(title=title,description=desc,image=image)

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
		
		await self.channel_layer.group_send(self.room_group_name, {"type": "chat.message", "message": message})

	async def chat_message(self, event):
		message = event["message"]
		await self.send(text_data=json.dumps({"message":message}))