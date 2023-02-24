from django.contrib import admin

from main.models import Event, ReservationCode


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "start_at", "end_at")


@admin.register(ReservationCode)
class ReservationCodeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "event", "code", "is_active")
