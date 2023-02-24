import random
import string

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


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

    @property
    def can_be_cancelled(self):
        no_longer_difference = self.end_at - self.start_at
        no_longer = 0 < no_longer_difference.days <= 2
        not_later_difference = self.start_at - timezone.now()
        not_later = 0 < not_later_difference.days >= 2
        return no_longer and not_later


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
    code = models.CharField(max_length=16, blank=True, verbose_name="Code")
    is_active = models.BooleanField(default=True, verbose_name="Is active")

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choice(
                string.ascii_lowercase + string.digits) for _ in range(16))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
        verbose_name = "Reservation code"
        verbose_name_plural = "Reservation codes"

    def __str__(self):
        return f'ReservationCode ({self.pk})'
