from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    start_at = models.DateTimeField(verbose_name="Start at")
    end_at = models.DateTimeField(verbose_name="End at")
    thumbnail = models.ImageField(verbose_name="Thumbnail", blank=True)
    users = models.ManyToManyField(
        User, related_name="events", blank=True, verbose_name="Users")

    class Meta:
        ordering = ['-id']
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title


class ReservationCode(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="codes",
        verbose_name="User",
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="codes",
        verbose_name="Event",
    )
    code = models.CharField(max_length=16, verbose_name="Code")

    class Meta:
        ordering = ['-id']
        verbose_name = "Reservation code"
        verbose_name_plural = "Reservation codes"

    def __str__(self):
        return f'ReservationCode ({self.pk})'
