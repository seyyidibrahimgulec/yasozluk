from rest_framework.generics import CreateAPIView

from interactions.models import Vote, Favorite
from interactions.serializers import VoteSerializer, FavoriteSerializer


class CreateVoteAPIView(CreateAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()


class CreateFavoriteAPIView(CreateAPIView):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
