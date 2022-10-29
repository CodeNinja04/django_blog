import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    username = models.CharField(max_length=150, verbose_name=_("username"), db_index=True, unique=True)
    first_name = models.CharField(max_length=150, verbose_name=_("first_name"))
    last_name = models.CharField(max_length=150, verbose_name=_("last_name"))
    email = models.EmailField(verbose_name=_("email"), db_index=True, unique=True)

    is_staff = models.BooleanField(default=False, verbose_name=_("is_staff"))
    is_active = models.BooleanField(default=True, verbose_name=_("is_active"))

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    def get_short_name(self):
        return self.first_name
