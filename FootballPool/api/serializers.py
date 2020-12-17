from api.models import Game
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        user = UserSerializer()
        model = Game
        fields = '__all__'
