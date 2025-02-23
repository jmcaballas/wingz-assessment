from factory import fuzzy, Faker, Sequence
from factory.django import DjangoModelFactory

from django.contrib.auth.hashers import make_password

from apps.users.models import User


class UserFactory(DjangoModelFactory[User]):
    username = Sequence(lambda n: f"user{n}")
    email = Faker("email")
    password = make_password("password")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    role = fuzzy.FuzzyChoice(User.RoleChoices)
    phone_number = "+639171234567"

    class Meta:
        model = User
