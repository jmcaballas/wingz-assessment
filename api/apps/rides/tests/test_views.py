import pytest
from rest_framework import status

from apps.rides.tests.factories import RideEventFactory, RideFactory
from apps.utils.test_models import TestModel


@pytest.mark.django_db
class TestRideViewSet(TestModel):
    namespace = "rides:rides-list"

    def test_list_unauthenticated(self, api_client):
        response = api_client.get(self.get_url())

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_non_admin(self, api_client, user):
        api_client.force_authenticate(user)
        response = api_client.get(self.get_url())

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list(self, api_client, admin_user):
        ride1 = RideFactory()
        ride2 = RideFactory()
        expected_ids = [ride1.pk, ride2.pk]

        api_client.force_authenticate(admin_user)
        response = api_client.get(self.get_url())

        ids = [item["id_ride"] for item in response.data["results"]]

        assert response.status_code == status.HTTP_200_OK
        assert set(expected_ids) == set(ids)


@pytest.mark.django_db
class TestRideEventViewSet(TestModel):
    namespace = "rides:ride-events-list"

    def test_list_unauthenticated(self, api_client):
        response = api_client.get(self.get_url())

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_non_admin(self, api_client, user):
        api_client.force_authenticate(user)
        response = api_client.get(self.get_url())

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list(self, api_client, admin_user):
        ride_event1 = RideEventFactory()
        ride_event2 = RideEventFactory()
        expected_ids = [ride_event1.pk, ride_event2.pk]

        api_client.force_authenticate(admin_user)
        response = api_client.get(self.get_url())

        ids = [item["id_ride_event"] for item in response.data["results"]]

        assert response.status_code == status.HTTP_200_OK
        assert set(expected_ids) == set(ids)
