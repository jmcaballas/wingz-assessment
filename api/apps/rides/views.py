from datetime import timedelta

from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from apps.rides.filters import RideFilter
from apps.rides.models import Ride, RideEvent
from apps.rides.serializers import RideEventSerializer, RideSerializer


class RideViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = RideFilter
    queryset = Ride.objects.prefetch_related(
        Prefetch(
            "ride_events",
            queryset=RideEvent.objects.filter(
                created_at__gte=timezone.now() - timedelta(days=1)
            ),
            to_attr="todays_ride_events",
        )
    )
    serializer_class = RideSerializer
    ordering_fields = ["pickup_time"]


class RideEventViewSet(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
