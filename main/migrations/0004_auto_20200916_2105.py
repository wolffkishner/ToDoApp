# Generated by Django 3.1.1 on 2020-09-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200916_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='fathers_name',
            field=models.CharField(blank=True, help_text="Enter your father's name", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='mothers_name',
            field=models.CharField(blank=True, help_text="Enter your mother's name", max_length=255, null=True),
        ),
    ]