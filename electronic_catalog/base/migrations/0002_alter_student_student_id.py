# Generated by Django 4.2.1 on 2024-02-25 18:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.UUIDField(default=uuid.UUID('9dacd820-d069-4648-88e8-a61e409dc470'), editable=False),
        ),
    ]
