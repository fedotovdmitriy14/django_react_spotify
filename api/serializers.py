from rest_framework import serializers

from api.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ('created_at',)

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')

class UpdateRoomSerializer(serializers.ModelSerializer):
    code = serializers.CharField(validators=[])                 # чтобы убрать unique

    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip', 'code')

