import json
import random
import urllib.parse
import urllib.request

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from contents.forms import EntryForm, TopicForm
from contents.models import Entry, Topic


class HomePageListView(ListView):
    context_object_name = "most_liked_entries"
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        kwargs["topics"] = Topic.objects.order_by("-entry__created_at")[:20]
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        if self.queryset is not None or self.model is not None:
            return super().get_queryset()
        return Entry.get_random_most_liked_entries()


class EntryListView(HomePageListView):
    context_object_name = "entries"
    template_name = "topic_entries.html"
    paginate_by = 10

    def get_queryset(self):
        return (
            Topic.objects.get(pk=self.kwargs["topic_pk"])
                .entry_set.order_by("created_at")
        )

    def get_context_data(self, **kwargs):
        kwargs["topic"] = Topic.objects.get(pk=self.kwargs["topic_pk"])
        return super().get_context_data(**kwargs)


@method_decorator(login_required, name="dispatch")
class NewTopicView(HomePageListView):
    template_name = "new_topic.html"

    def get_context_data(self, **kwargs):
        kwargs["topic_form"] = TopicForm()
        kwargs["entry_form"] = EntryForm()
        return super().get_context_data(**kwargs)

    def post(self, request):
        topic_form = TopicForm(request.POST)
        entry_form = EntryForm(request.POST)

        if topic_form.is_valid() and entry_form.is_valid():
            topic = topic_form.save()

            entry = entry_form.save(commit=False)
            entry.topic = topic
            entry.created_by = request.user
            entry.save()

            return redirect("topic_entries", topic_pk=topic.pk)


def today_in_history(request):
    url = "http://history.muffinlabs.com/date"
    f = urllib.request.urlopen(url)
    str_res = f.read().decode('utf-8')
    result = json.loads(str_res)
    k = 3
    events = random.choices(result["data"]['Events'], k=k)
    births = random.choices(result["data"]['Births'], k=k)
    deaths = random.choices(result["data"]['Deaths'], k=k)
    return JsonResponse({
        "events": events,
        "births": births,
        "deaths": deaths
    })


class TopicSearchListView(HomePageListView):
    # TODO: Daha sonra kanallar ve kullanıcıllar içerisinden arama da eklenicek.
    template_name = 'search.html'
    context_object_name = "topics_search"

    def get_queryset(self):
        q = self.request.GET.get('search_q')
        if q:
            return (
                Topic.objects.filter(subject__icontains=q)[0:10]
            )
        return Topic.objects.filter()[0:10]
