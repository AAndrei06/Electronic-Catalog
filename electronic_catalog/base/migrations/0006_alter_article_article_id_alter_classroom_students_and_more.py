# Generated by Django 5.0.2 on 2024-03-03 17:19

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_article_article_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_id',
            field=models.UUIDField(default=uuid.UUID('153b2ac2-5535-4195-ba4c-857498053796'), editable=False),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='students',
            field=models.ManyToManyField(blank=True, to='base.student'),
        ),
        migrations.AlterField(
            model_name='homeworktodo',
            name='homework_id',
            field=models.UUIDField(default=uuid.UUID('92cd467e-0589-4c8f-b73c-3afe529e01f0'), editable=False),
        ),
        migrations.AlterField(
            model_name='homeworktodo',
            name='received_homework',
            field=models.ManyToManyField(blank=True, to='base.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.UUIDField(default=uuid.UUID('2b1acd7c-9448-46e1-b8ba-4b734912c1ac')),
        ),
    ]