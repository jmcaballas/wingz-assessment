from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils.utils import max_len_choices


class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = "Admin", _("Admin")
        USER = "User", _("User")

    email = models.EmailField(_("email address"), max_length=150, unique=True)
    role = models.CharField(
        _("role"),
        max_length=max_len_choices(RoleChoices),
        choices=RoleChoices.choices,
        default=RoleChoices.USER,
    )
    phone_number = PhoneNumberField(_("phone number"), blank=True)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
