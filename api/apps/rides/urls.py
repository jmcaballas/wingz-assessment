from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.rides.views import RideEventViewSet, RideViewSet


app_name = "rides"

router = SimpleRouter()
router.register(r"events", RideEventViewSet, basename="ride-events")
router.register(r"", RideViewSet, basename="rides")

urlpatterns = [
    path("", include(router.urls)),
]
