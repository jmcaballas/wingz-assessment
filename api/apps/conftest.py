import pytest
from rest_framework.test import APIClient

from apps.users.tests.factories import UserFactory


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def user():
    return UserFactory(role="User")


@pytest.fixture
def admin_user():
    return UserFactory(role="Admin")
