from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    starter_user = models.ForeignKey(to=User, on_delete=models.PROTECT)
    channels = models.ManyToManyField(to='Channel')


class Entry(models.Model):
    text = models.TextField()
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Channel(models.Model):
    name = models.CharField(max_length=255)
