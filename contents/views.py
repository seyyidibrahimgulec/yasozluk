import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.generic import ListView

from contents.forms import NewTopicForm
from contents.models import Entry, Topic, Channel


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
    # all topics are being fetched at the moment.
    # will be put some kind of pagination over here
    # or will be moved to somewhere else
    topics = Topic.objects.order_by("-id")
    topicEntries = Entry.objects.filter(topic__pk=num).order_by("-created_at")
    currentTopic = Topic.objects.get(pk=num)
    channels = currentTopic.channels.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(topicEntries, 10)  # Show 25 contacts per page.
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        entries = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        entries = paginator.page(paginator.num_pages)

    return render(request, 'topicEntries.html',
                  {'entries': entries, 'topics': topics, 'currentTopic': currentTopic, 'channels': channels})


def newTopic(request):
    topics = Topic.objects.order_by("-id")
    channels = Channel.objects.all().order_by("name")

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            newSaved = form.save()
            print("saved with:", newSaved.pk)
            return redirect('topicEntries', num=newSaved.pk)
    else:
        form = NewTopicForm()
    return render(request, 'newTopic.html', {'form': form, 'topics': topics, 'channels': channels})


def tonumeric(s, default):
    try:
        return int(s)
    except Exception:
        return default
