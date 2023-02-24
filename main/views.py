from django.views.generic.base import TemplateView
from rest_framework.generics import GenericAPIView, ListAPIView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from main.models import Event, ReservationCode
from main.serializers import EventSerializer, ReservationCodeSerializer


class MainLoginView(LoginView):
    template_name = "main/login.html"


class MainLogoutView(LogoutView):
    template_name = "main/logout.html"
    next_page = "/login/"


class AllEventsView(LoginRequiredMixin, TemplateView):
    template_name = "main/events.html"


class EventListView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class RegisterToEventView(GenericAPIView):

    def post(self, request, *args, **kwargs):
        pass


class CancelRegistrationView(GenericAPIView):
    pass
