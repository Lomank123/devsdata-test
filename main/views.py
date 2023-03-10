from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.views.generic.base import TemplateView
from rest_framework import status
from rest_framework.exceptions import APIException, NotFound
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Exists, OuterRef

from main.consts import CANNOT_CANCEL_ERROR_MSG
from main.models import Event, ReservationCode
from main.serializers import (
    CancelRegistrationSerializer,
    EventSerializer,
    RegisterToEventSerializer,
)


class MainLoginView(LoginView):
    template_name = "main/login.html"


class MainLogoutView(LogoutView):
    template_name = "main/logout.html"
    next_page = "/login/"


class AllEventsView(LoginRequiredMixin, TemplateView):
    template_name = "main/events.html"


class EventListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.annotate(is_user=Exists(
            ReservationCode.objects.filter(
                event_id=OuterRef("pk"), user=self.request.user, is_active=True)
        ))


class RegisterToEventView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterToEventSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        event_id = serializer.data.get('event_id')
        user = request.user
        event = Event.objects.filter(id=event_id).first()

        # Create model object
        reg_code = ReservationCode.objects.create(user=user, event=event)
        # Update m2m field
        event.users.add(user)
        event.save()

        return Response(
            status=status.HTTP_201_CREATED, data={'code': reg_code.code})


class CancelRegistrationView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CancelRegistrationSerializer

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        code = serializer.data.get("code")
        # Find and update reg code data
        reg_code = ReservationCode.objects.filter(
            user=user, code=code, is_active=True).first()
        if reg_code is None:
            raise NotFound(code=status.HTTP_400_BAD_REQUEST)
        reg_code.is_active = False
        reg_code.save(update_fields=["is_active"])

        # Update event data
        event = reg_code.event
        if not event.can_be_cancelled:
            raise APIException(
                detail=CANNOT_CANCEL_ERROR_MSG,
                code=status.HTTP_400_BAD_REQUEST
            )
        # Update m2m field
        event.users.remove(user)
        event.save()

        return Response(data=dict())
