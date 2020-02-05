from rest_framework import serializers, viewsets
from .models import Room, Inventory, Proof


class RoomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Room
        fields = ('room_id', 'title', 'description', 'coordinates', 'players', 'items', 'exits', 'cooldown', 'errors', 'messages' )

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()