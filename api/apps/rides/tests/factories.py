from datetime import timezone

from factory import fuzzy, Faker, SubFactory

from apps.utils.factories import TimeStampedModelFactory
from apps.users.tests.factories import UserFactory
from apps.rides.models import Ride, RideEvent


class RideFactory(TimeStampedModelFactory):
    status = fuzzy.FuzzyChoice(Ride.StatusChoices)
    id_rider = SubFactory(UserFactory)
    id_driver = SubFactory(UserFactory)
    pickup_latitude = Faker("latitude")
    pickup_longitude = Faker("longitude")
    dropoff_latitude = Faker("latitude")
    dropoff_longitude = Faker("longitude")
    pickup_time = Faker("date_time_this_year", tzinfo=timezone.utc)

    class Meta:
        model = Ride


class RideEventFactory(TimeStampedModelFactory):
    id_ride = SubFactory(RideFactory)
    description = Faker("text", max_nb_chars=255)

    class Meta:
        model = RideEvent
