from rest_framework.generics import CreateAPIView

from django.contrib.auth.models import User

from contents.models import Entry, Topic
from contents.serializers import EntrySerializer


class CreateEntryAPIView(CreateAPIView):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()
