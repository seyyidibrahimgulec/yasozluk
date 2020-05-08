from django.contrib.auth.models import User
from django.db import models
from enumfields import EnumField

from contents.models import Entry
from interactions.enums import VoteType


class Vote(models.Model):
    vote = EnumField(enum=VoteType, null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    entry = models.ForeignKey(to=Entry, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.vote)


class Block(models.Model):
    blocked_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='blocked_by')
    blocked_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='blocked_user')


class Favorite(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    entry = models.ForeignKey(to=Entry, on_delete=models.CASCADE)


class Message(models.Model):
    text = models.TextField()
    send_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='send_by')
    send_to = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='send_to')
    created_at = models.DateTimeField(auto_now_add=True)
