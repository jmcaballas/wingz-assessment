from datetime import timezone

import factory
from factory.django import DjangoModelFactory


class TimeStampedModelFactory(DjangoModelFactory):
    created_at = factory.Faker("date_time_this_year", tzinfo=timezone.utc)
    updated_at = factory.Faker("date_time_this_year", tzinfo=timezone.utc)

    class Meta:
        abstract = True
