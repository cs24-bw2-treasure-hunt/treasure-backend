from rest_framework import serializers, viewsets
from .models import Room, Inventory, Proof

# Room
class RoomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Room
        fields = ('room_id', 'title', 'description', 'coordinates', 'players', 'items', 'exits', 'cooldown', 'errors', 'messages' )

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    

# Inventory
class InventorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Inventory
        fields = ('name','cooldown', 'encumbrance', 'strength', 'speed', 'gold', 'bodywear', 'footwear',  'errors', 'messages' )

class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()

# Proof
class ProofSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Proof
        fields = ('proof','difficulty', 'cooldown', 'errors', 'messages' )

class ProofViewSet(viewsets.ModelViewSet):
    serializer_class = ProofSerializer
    queryset = Inventory.objects.all()

