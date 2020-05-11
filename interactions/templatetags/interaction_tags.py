from django import template
from django.contrib.auth.models import User

from contents.models import Entry
from interactions.models import Favorite, Vote


register = template.Library()


@register.simple_tag
def is_voted(entry_pk, user_pk):
    try:
        return Vote.objects.get(
            entry=Entry.objects.get(pk=entry_pk), user=User.objects.get(pk=user_pk)
        )
    except Exception:
        return False


@register.simple_tag
def is_favorited(entry_pk, user_pk):
    try:
        return Favorite.objects.get(
            entry=Entry.objects.get(pk=entry_pk), user=User.objects.get(pk=user_pk)
        )
    except Exception:
        return False
