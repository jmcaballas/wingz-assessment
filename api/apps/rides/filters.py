import django_filters
from django.db.models import F, FloatField, ExpressionWrapper
from django.db.models.functions import Power
from apps.rides.models import Ride


class RideFilter(django_filters.FilterSet):
    rider_email = django_filters.CharFilter(
        field_name="id_rider__email", lookup_expr="iexact"
    )
    pickup_latitude = django_filters.NumberFilter(
        method="filter_by_distance", label="Pickup Latitude"
    )
    pickup_longitude = django_filters.NumberFilter(
        method="filter_by_distance", label="Pickup Longitude"
    )

    class Meta:
        model = Ride
        fields = ["status", "rider_email"]

    def filter_by_distance(self, queryset, name, value):
        lat = self.data.get("pickup_latitude")
        lng = self.data.get("pickup_longitude")

        if lat and lng:
            try:
                lat = float(lat)
                lng = float(lng)

                # Compute squared Euclidean distance for sorting
                distance_expr = ExpressionWrapper(
                    Power(F("pickup_latitude") - lat, 2)
                    + Power(F("pickup_longitude") - lng, 2),
                    output_field=FloatField(),
                )

                queryset = queryset.annotate(distance=distance_expr).order_by(
                    "distance"
                )

            except ValueError:
                pass

        return queryset
