from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class TaskInfo(models.Model):
    IMPORTANCE = (('Very Low', 'Very Low'), ('Low', 'Low'), ('Medium',
                                                             'Medium'), ('High', 'High'), ('Very High', 'Very High'))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, related_name='taskinfo', blank=True)
    task = models.CharField(max_length=255, null=True)
    deadline = models.DateField(null=True)
    notes = models.TextField(max_length=500, null=True, blank=True)
    importance = models.CharField(
        max_length=255, null=True, blank=True, choices=IMPORTANCE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
