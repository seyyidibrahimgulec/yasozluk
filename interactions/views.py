from django.http import JsonResponse

from contents.models import Entry
from interactions.enums import VoteType
from interactions.models import Vote


def addVote(request):
    entryId = request.POST.get("entryId")
    value = request.POST.get("value")
    entry = Entry.objects.get(pk=entryId)
    user = request.user
    type = VoteType.upvote
    if value == -1:
        type = VoteType.downvote

    vote = Vote(vote=type, user=user, entry=entry)
    vote.save()

    data = {
        'success': True,
        "id": vote.pk
    }
    return JsonResponse(data)
