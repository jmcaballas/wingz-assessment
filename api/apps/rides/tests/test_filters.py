import pytest
from datetime import timedelta
from django.utils import timezone

from apps.rides.filters import RideFilter
from apps.rides.models import Ride
from apps.rides.tests.factories import RideFactory
from apps.users.tests.factories import UserFactory


@pytest.mark.django_db
class TestRideFilter:
    def test_filter_by_status(self):
        ride1 = RideFactory(status=Ride.StatusChoices.PICKUP)
        RideFactory(status=Ride.StatusChoices.DROPOFF)

        expected_ids = {ride1.id_ride}

        queryset = Ride.objects.all()
        filtered_queryset = RideFilter(
            data={"status": Ride.StatusChoices.PICKUP}, queryset=queryset
        ).qs

        assert set(filtered_queryset.values_list("id_ride", flat=True)) == expected_ids

    def test_filter_by_rider_email(self):
        rider1 = UserFactory(email="rider1@example.com")
        rider2 = UserFactory(email="rider2@example.com")

        ride1 = RideFactory(id_rider=rider1)
        RideFactory(id_rider=rider2)

        expected_ids = {ride1.id_ride}

        queryset = Ride.objects.all()
        filtered_queryset = RideFilter(
            data={"rider_email": "rider1@example.com"}, queryset=queryset
        ).qs

        assert set(filtered_queryset.values_list("id_ride", flat=True)) == expected_ids

    def test_sort_by_pickup_time(self):
        now = timezone.now()
        ride1 = RideFactory(pickup_time=now)
        ride2 = RideFactory(pickup_time=now + timedelta(hours=1))

        queryset = Ride.objects.all()
        filtered_queryset = RideFilter(queryset=queryset).qs.order_by("pickup_time")

        assert filtered_queryset.first().id_ride == ride1.id_ride
        assert filtered_queryset.last().id_ride == ride2.id_ride

        filtered_queryset = RideFilter(queryset=queryset).qs.order_by("-pickup_time")

        assert filtered_queryset.first().id_ride == ride2.id_ride
        assert filtered_queryset.last().id_ride == ride1.id_ride

    def test_sort_by_distance(self):
        ride1 = RideFactory(pickup_latitude=40.748817, pickup_longitude=-73.985428)
        ride2 = RideFactory(pickup_latitude=34.052235, pickup_longitude=-118.243683)
        test_lat = 34.052235
        test_lng = -118.243683

        queryset = Ride.objects.all()
        filtered_queryset = RideFilter(
            data={"pickup_latitude": test_lat, "pickup_longitude": test_lng},
            queryset=queryset,
        ).qs
        sorted_rides = filtered_queryset.order_by("distance")

        assert sorted_rides.first().id_ride == ride2.id_ride
        assert sorted_rides.last().id_ride == ride1.id_ride
