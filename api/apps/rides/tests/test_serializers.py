import pytest

from apps.rides.serializers import RideEventSerializer, RideSerializer
from apps.rides.tests.factories import RideEventFactory, RideFactory


@pytest.mark.django_db
class TestRideSerializer:
    def test_ride_serializer(self):
        ride = RideFactory()
        ride_event = RideEventFactory(id_ride=ride)
        ride.todays_ride_events = [ride_event]
        serializer = RideSerializer(ride)

        todays_ride_events = [
            {
                "id_ride_event": ride_event.id_ride_event,
                "id_ride": ride_event.id_ride.id_ride,
                "description": ride_event.description,
                "created_at": ride_event.created_at.isoformat().replace("+00:00", "Z"),
            }
        ]

        assert serializer.data == {
            "id_ride": ride.id_ride,
            "status": ride.status,
            "id_rider": ride.id_rider.id_user,
            "id_driver": ride.id_driver.id_user,
            "pickup_latitude": float(ride.pickup_latitude),
            "pickup_longitude": float(ride.pickup_longitude),
            "dropoff_latitude": float(ride.dropoff_latitude),
            "dropoff_longitude": float(ride.dropoff_longitude),
            "pickup_time": ride.pickup_time.isoformat().replace("+00:00", "Z"),
            "todays_ride_events": todays_ride_events,
        }


@pytest.mark.django_db
class TestRideEventSerializer:
    def test_ride_serializer(self):
        ride_event = RideEventFactory()
        serializer = RideEventSerializer(ride_event)
        assert serializer.data == {
            "id_ride_event": ride_event.id_ride_event,
            "id_ride": ride_event.id_ride.id_ride,
            "description": ride_event.description,
            "created_at": ride_event.created_at.isoformat().replace("+00:00", "Z"),
        }
