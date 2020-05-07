from rest_framework.generics import CreateAPIView

from contents.models import Entry
from contents.serializers import EntrySerializer


class CreateEntryAPIView(CreateAPIView):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()
