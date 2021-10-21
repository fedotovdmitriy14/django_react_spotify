from rest_framework import serializers

from api.models import Room


class RoomSerializer(serializers.Serializer):
    class Meta:
        model = Room
        exclude = ('created_at',)

