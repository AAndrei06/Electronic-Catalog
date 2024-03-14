from celery import shared_task
from .models import Article

@shared_task
def add():
	for art in Article.objects.all():
		art.delete()
