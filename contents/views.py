import datetime
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
