# Generated by Django 5.0.2 on 2024-03-04 17:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_article_article_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='student_obj',
        ),
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.ManyToManyField(to='base.mark'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_id',
            field=models.UUIDField(default=uuid.UUID('6d585c59-7de0-436e-97d4-0fdd4a380b97'), editable=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='homeworktodo',
            name='homework_id',
            field=models.UUIDField(default=uuid.UUID('b01e929a-f924-417b-aefc-956817b3e712'), editable=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.UUIDField(default=uuid.UUID('6c196a41-b1af-44e5-b575-5152c50736df')),
        ),
    ]
