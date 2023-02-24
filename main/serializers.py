from rest_framework import serializers

from main.consts import CANNOT_CANCEL_ERROR_MSG
from main.models import Event, ReservationCode
from rest_framework import status


class EventSerializer(serializers.ModelSerializer):
    is_user = serializers.BooleanField()

    class Meta:
        model = Event
        fields = ("title", "id", "start_at", "end_at", "can_be_cancelled", "is_user")


class ReservationCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReservationCode
        fields = "__all__"


class RegisterToEventSerializer(serializers.Serializer):
    event_id = serializers.IntegerField()


class CancelRegistrationSerializer(serializers.Serializer):
    code = serializers.CharField()
    can_be_cancelled = serializers.BooleanField()

    def validate_can_be_cancelled(self, value):
        if not value:
            raise serializers.ValidationError(
                CANNOT_CANCEL_ERROR_MSG,
                code=status.HTTP_400_BAD_REQUEST
            )
        return value
