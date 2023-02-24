from rest_framework import serializers
from main.models import Event, ReservationCode


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"


class ReservationCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReservationCode
        fields = "__all__"
