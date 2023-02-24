from django.urls import path

from main.views import (
    AllEventsView,
    CancelRegistrationView,
    EventListView,
    RegisterToEventView,
)

urlpatterns = [
    # Default
    path("all/", AllEventsView.as_view(), name="all-events"),
    # API
    path("fetch-all/", EventListView.as_view(), name="event-list"),
    path("register/", RegisterToEventView.as_view(), name="register-to-event"),
    path(
        "cancel/",
        CancelRegistrationView.as_view(),
        name="cancel-registration",
    ),
]
