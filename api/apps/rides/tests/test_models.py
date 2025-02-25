import pytest
from django.db import IntegrityError

from apps.users.tests.factories import UserFactory
from apps.rides.models import Ride, RideEvent
from .factories import RideFactory, RideEventFactory


@pytest.mark.django_db
class TestRide:
    def test_all_fields(self):
        user1 = UserFactory.create()
        user2 = UserFactory.create()
        ride = RideFactory.create(
            status=Ride.StatusChoices.EN_ROUTE,
            id_rider=user1,
            id_driver=user2,
            pickup_latitude=35.6595,
            pickup_longitude=139.7005,
            dropoff_latitude=35.6940,
            dropoff_longitude=139.7038,
            pickup_time="2025-02-25T12:00:00Z",
        )

        db_ride = Ride.objects.get(pk=ride.pk)
        assert db_ride.status == Ride.StatusChoices.EN_ROUTE
        assert db_ride.pickup_latitude == 35.6595
        assert db_ride.pickup_longitude == 139.7005
        assert db_ride.dropoff_latitude == 35.6940
        assert db_ride.dropoff_longitude == 139.7038
        assert db_ride.pickup_time.isoformat() == "2025-02-25T12:00:00+00:00"

    def test_rider_and_driver_must_be_different(self):
        user = UserFactory.create()

        with pytest.raises(IntegrityError):
            RideFactory(id_rider=user, id_driver=user)


@pytest.mark.django_db
class TestRideEvent:
    def test_minimal_fields(self):
        ride_event = RideEventFactory.create(description="")

        db_ride_event = RideEvent.objects.get(pk=ride_event.pk)
        assert db_ride_event.id_ride is not None
        assert db_ride_event.description == ""
        assert db_ride_event.created_at is not None

    def test_all_fields(self):
        ride_event = RideEventFactory.create(
            description="Driver has arrived at pickup location."
        )

        db_ride_event = RideEvent.objects.get(pk=ride_event.pk)
        assert db_ride_event.id_ride == ride_event.id_ride
        assert db_ride_event.description == "Driver has arrived at pickup location."
        assert db_ride_event.created_at == ride_event.created_at
