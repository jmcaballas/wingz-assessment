import pytest

from apps.users.serializers import UserSerializer
from apps.users.tests.factories import UserFactory


@pytest.mark.django_db
class TestUserSerializer:
    def test_user_serializer(self):
        user = UserFactory()
        serializer = UserSerializer(user)
        assert serializer.data == {
            "id_user": user.id_user,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone_number": user.phone_number,
            "role": user.role,
        }
