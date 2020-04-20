import datetime

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from contents.models import Entry, Topic


class HomePageListView(ListView):
    model = Topic
    queryset = Topic.objects.filter(
        entry__created_at__startswith=datetime.date.today()
    ).order_by("-entry__created_at")
    context_object_name = "topics"
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        kwargs["most_liked_entries"] = Entry.get_random_most_liked_entries()
        return super().get_context_data(**kwargs)


def entryListView(request, num=-1):
    topicId = num
    # all topics are being fetched at the moment.
    # will be put some kind of pagination over here
    # or will be moved to somewhere else
    topics = Topic.objects.order_by("-entry__created_at")
    entries = Entry.objects.filter(topic__pk=topicId).order_by("-created_at")
    currentTopic = Topic.objects.get(pk=topicId)
    channels = currentTopic.channels.all()

    paginator = Paginator(entries, 10)  # Show 25 contacts per page.
    page_number = tonumeric(request.GET.get('page'), 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'topicEntries.html',
                  {'page_obj': page_obj, 'topics': topics, 'currentTopic': currentTopic, 'channels': channels,
                   'pageCount': paginator.num_pages})


def tonumeric(s, default):
    try:
        return int(s)
    except Exception:
        return default
