# Generated by Django 3.1.1 on 2020-09-17 10:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200917_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskinfo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
