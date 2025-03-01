from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id_user",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "role",
        ]
        read_only_fields = ["id_user"]
