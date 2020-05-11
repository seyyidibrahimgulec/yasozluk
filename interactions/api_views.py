from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView

from interactions.models import Vote, Favorite
from interactions.serializers import VoteSerializer, FavoriteSerializer

from rest_framework.mixins import UpdateModelMixin, CreateModelMixin


class CreateVoteAPIView(CreateAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()


class CreateFavoriteAPIView(CreateAPIView):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()


class DestroyVoteAPIView(DestroyAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()


class DestroyFavoriteAPIView(DestroyAPIView):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
