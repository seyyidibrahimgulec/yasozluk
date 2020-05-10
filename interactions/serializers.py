from rest_framework import serializers

from interactions.models import Vote, Favorite


class VoteSerializer(serializers.ModelSerializer):
    vote = serializers.CharField()
    
    class Meta:
        model = Vote
        fields = '__all__'

        
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'        
