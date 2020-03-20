import os
import sys
from random import randint, random

from django.db import transaction
from django.core.wsgi import get_wsgi_application


proj_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yasozluk.settings')
sys.path.append(proj_path)
os.chdir(proj_path)
application = get_wsgi_application()


from django.contrib.auth.models import User
from contents.models import Topic, Entry, Channel
from interactions.models import Vote, Favorite
from interactions.enums import VoteType

channel_names = ['Spor', 'Ekonomi', 'Politika', 'Eğitim', 'Edebiyat',
            'Bilim', 'Haber', 'Sinema', 'Müzik', 'Tarih', 'Moda',
            'Sanat', 'Otomotiv', 'Magazin', 'Sağlık', 'Oyun',
            'Programlama', 'Seyahat', 'Havacılık', 'Anket', ]




# Users
for i in range(100):
    user, created = User.objects.get_or_create(username="Yazar {}".format(i+1))
    print("Created {} user".format(user.username))

# Channels
for name in channel_names:
    Channel.objects.get_or_create(name=name)
    print("Created {} channel".format(name))

# Topics
for i in range(100):
    subject = "Subject {}".format(i+1)
    starter_user = User.objects.get(pk=randint(1, 100))
    topic, created = Topic.objects.get_or_create(subject=subject,
                                                 starter_user=starter_user)
    topic.channels.add(Channel.objects.get(pk=randint(1, len(channel_names))))
    topic.channels.add(Channel.objects.get(pk=randint(1, len(channel_names))))
    topic.save()
    print("Created {} topic by {}".format(subject, starter_user))

# Entries
for i in range(100):
    text = "Test Entry {}".format(i+1)
    topic = Topic.objects.get(pk=randint(1, 100))
    created_by = User.objects.get(pk=randint(1, 100))
    entry, created = Entry.objects.get_or_create(text=text, topic=topic,
                                                 created_by=created_by)
    print("Created entry in {} by {}".format(topic.subject, created_by))

# Votes
for i in range(100):
    user = User.objects.get(pk=randint(1, 100))
    entry = Entry.objects.get(pk=randint(1, 100))
    Vote.objects.update_or_create(user=user, entry=entry,
                                  vote=VoteType.upvote)
    print("Created upvote in {}th entry by {}".format(entry.pk, user))
    user = User.objects.get(pk=randint(1, 100))
    entry = Entry.objects.get(pk=randint(1, 100))
    Vote.objects.update_or_create(user=user, entry=entry,
                                  vote=VoteType.downvote)
    print("Created downvote in {}th entry by {}".format(entry.pk, user))

# Favorites
for i in range(100):
    user = User.objects.get(pk=randint(1, 100))
    entry = Entry.objects.get(pk=randint(1, 100))
    Favorite.objects.get_or_create(user=user, entry=entry)
    print("Created favorite in {}th entry by {}".format(entry.pk, user))
