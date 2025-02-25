from django.conf import settings
from django.db import models
from django.db.models import F, Q
from django.utils.translation import gettext_lazy as _

from apps.utils.models import TimeStampedModel
from apps.utils.utils import max_len_choices


class Ride(TimeStampedModel):
    class StatusChoices(models.TextChoices):
        PICKUP = "Pickup", _("Pickup")
        EN_ROUTE = "En Route", _("En Route")
        DROPOFF = "Dropoff", _("Dropoff")

    id_ride = models.AutoField(primary_key=True)
    status = models.CharField(
        _("status"),
        max_length=max_len_choices(StatusChoices),
        choices=StatusChoices.choices,
        default=StatusChoices.PICKUP,
    )
    id_rider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("rider"),
        on_delete=models.PROTECT,
        related_name="rides_as_rider",
    )
    id_driver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("driver"),
        on_delete=models.PROTECT,
        related_name="rides_as_driver",
    )
    pickup_latitude = models.FloatField(_("pickup latitude"))
    pickup_longitude = models.FloatField(_("pickup longitude"))
    dropoff_latitude = models.FloatField(_("dropoff latitude"))
    dropoff_longitude = models.FloatField(_("dropoff longitude"))
    pickup_time = models.DateTimeField(_("pickup time"))

    class Meta:
        verbose_name = _("rides")
        verbose_name_plural = _("rides")
        constraints = [
            models.CheckConstraint(
                check=~Q(id_rider=F("id_driver")),
                name="check_rider_not_driver",
            )
        ]

    def __str__(self):
        return f"{self.pickup_time} - {self.status} (#{self.id_ride})"


class RideEvent(TimeStampedModel):
    id_ride_event = models.AutoField(primary_key=True)
    id_ride = models.ForeignKey(
        Ride,
        verbose_name=_("ride"),
        on_delete=models.CASCADE,
        related_name="ride_events",
    )
    description = models.CharField(_("description"), max_length=255, blank=True)

    class Meta:
        verbose_name = _("ride event")
        verbose_name_plural = _("ride events")

    def __str__(self):
        return f"Ride Event for Ride #{self.id_ride.id_ride}"
