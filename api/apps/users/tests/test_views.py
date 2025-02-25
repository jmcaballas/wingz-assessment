import pytest
from rest_framework import status

from apps.users.tests.factories import UserFactory
from apps.utils.test_models import TestModel


@pytest.mark.django_db
class TestUserViewSet(TestModel):
    namespace = "users:users-list"

    def test_list_unauthenticated(self, api_client):
        response = api_client.get(self.get_url())

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_non_admin(self, api_client, user):
        api_client.force_authenticate(user)
        response = api_client.get(self.get_url())

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list(self, api_client, admin_user):
        user1 = UserFactory()
        user2 = UserFactory()
        expected_ids = [admin_user.id_user, user1.pk, user2.pk]

        api_client.force_authenticate(admin_user)
        response = api_client.get(self.get_url())

        ids = [item["id_user"] for item in response.data["results"]]

        assert response.status_code == status.HTTP_200_OK
        assert set(expected_ids) == set(ids)
