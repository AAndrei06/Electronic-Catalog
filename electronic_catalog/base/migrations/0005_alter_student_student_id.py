# Generated by Django 5.0.2 on 2024-03-01 15:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.UUIDField(default=uuid.UUID('089c1fae-1654-49d9-a239-557625368313'), editable=False),
        ),
    ]
