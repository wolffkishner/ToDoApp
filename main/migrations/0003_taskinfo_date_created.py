# Generated by Django 3.1.1 on 2020-09-22 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_taskinfo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskinfo',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
