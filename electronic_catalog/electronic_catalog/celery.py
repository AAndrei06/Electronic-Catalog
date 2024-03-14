from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electronic_catalog.settings')

app = Celery('electronic_catalog')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()