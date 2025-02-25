from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.users.views import UserViewSet


app_name = "users"

router = SimpleRouter()
router.register(r"", UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
]
