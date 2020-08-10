import datetime
from random import sample

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, Q

from interactions.enums import VoteType


class Topic(models.Model):
    subject = models.CharField(max_length=255, unique=True)
    channels = models.ManyToManyField(to="Channel")

    @property
    def updated_at(self):
        return self.entry_set.order_by("-created_at").first().updated_at

    def get_today_entry_count(self):
        return self.entry_set.filter(
            created_at__startswith=datetime.date.today()
        ).count()

    def get_entry_set(self):
        return self.entry_set.count()


class Entry(models.Model):
    text = models.TextField()
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    @property
    def upvote_count(self):
        return self.vote_set.filter(vote=VoteType.upvote).count()

    @property
    def downvote_count(self):
        return self.vote_set.filter(vote=VoteType.downvote).count()

    @property
    def favorite_count(self):
        return self.favorite_set.count()

    def get_random_most_liked_entries(top_n=20, pick_n=5):
        # TODO: increase top_n after database increased
        #elmaa
        """
        Returns random "pick_n" entries of most liked "top_n" entries
        """
        upvotes = Count("vote", filter=Q(vote__vote=VoteType.upvote))
        downvotes = Count("vote", filter=Q(vote__vote=VoteType.downvote))
        score = upvotes - downvotes
        return sample(
            list(Entry.objects.annotate(score=score).order_by("-score")[:top_n]), pick_n
        )


class Channel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
