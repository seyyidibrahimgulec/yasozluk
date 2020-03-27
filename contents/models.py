from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count, Q

from interactions.enums import VoteType


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

    @property
    def upvotes(self):
        return self.vote_set.filter(vote=VoteType.upvote).count()

    @property
    def downvotes(self):
        return self.vote_set.filter(vote=VoteType.downvote).count()

    def get_random_most_liked_entries(top_n=20, pick_n=5):
        # TODO: increase top_n after database increased
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
