from rest_framework import viewsets

from apps.users.models import User
from apps.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
