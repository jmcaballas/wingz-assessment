from rest_framework import viewsets

from apps.rides.models import Ride, RideEvent
from apps.rides.serializers import RideEventSerializer, RideSerializer


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer


class RideEventViewSet(viewsets.ModelViewSet):
    queryset = RideEvent.objects.all()
    serializer_class = RideEventSerializer
