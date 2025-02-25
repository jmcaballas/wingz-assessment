from rest_framework import serializers

from apps.rides.models import Ride, RideEvent


class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = [
            "id_ride_event",
            "id_ride",
            "description",
            "created_at",
        ]
        read_only_fields = ["id_ride_event"]


class RideSerializer(serializers.ModelSerializer):
    todays_ride_events = RideEventSerializer(many=True)

    class Meta:
        model = Ride
        fields = [
            "id_ride",
            "status",
            "id_rider",
            "id_driver",
            "pickup_latitude",
            "pickup_longitude",
            "dropoff_latitude",
            "dropoff_longitude",
            "pickup_time",
            "todays_ride_events",
        ]
        read_only_fields = ["id_ride"]
