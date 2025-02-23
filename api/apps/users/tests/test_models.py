import pytest
from django.db import IntegrityError

from apps.users.models import User

from .factories import UserFactory


@pytest.mark.django_db
class TestUser:
    def test_minimal_fields(self):
        user = UserFactory.create(
            first_name="",
            last_name="",
            phone_number="",
        )

        db_user = User.objects.get(pk=user.pk)
        assert db_user.first_name == ""
        assert db_user.last_name == ""
        assert db_user.phone_number == ""

    def test_all_fields(self):
        user = UserFactory.create(
            username="testuser",
            email="test@user.com",
            password="password",
            first_name="Test",
            last_name="User",
            role="ADMIN",
            phone_number="+639171234567",
        )

        db_user = User.objects.get(pk=user.pk)
        assert db_user.username == "testuser"
        assert db_user.email == "test@user.com"
        assert db_user.password == "password"
        assert db_user.first_name == "Test"
        assert db_user.last_name == "User"
        assert db_user.role == "ADMIN"
        assert db_user.phone_number == "+639171234567"

    def test_fail_duplicate_username(self):
        UserFactory.create(username="testuser")
        with pytest.raises(IntegrityError):
            UserFactory.create(username="testuser")

    def test_fail_duplicate_email(self):
        UserFactory.create(email="test@user.com")
        with pytest.raises(IntegrityError):
            UserFactory.create(email="test@user.com")
