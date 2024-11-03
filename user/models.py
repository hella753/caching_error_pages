from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, password, **other_fields):
        if not username:
            raise ValueError("Required Field Email is not set")
        if not password:
            raise ValueError("Required Field Password is not set")
        user = self.model(username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **other_fields):
        if not username:
            raise ValueError("Required Field Email is not set")
        if not password:
            raise ValueError("Required Field Password is not set")
        user = self.create_user(username, password, **other_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    id = models.AutoField(primary_key=True)
    email = models.EmailField(
        "email address",
        max_length=50,
        blank=True,
        null=True
    )
    username = models.CharField(
        "username",
        max_length=20,
        unique=True,
        help_text="Required. 20 characters or fewer",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists."
        }
    )
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(
        "first name",
        max_length=150,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        "last name",
        max_length=150,
        blank=True,
        null=True
    )
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField("active", default=True)

    order_address = models.CharField(max_length=100, verbose_name="მისამართი", null=True, blank=True)
    city = models.CharField("ქალაქი", max_length=100, null=True, blank=True)
    country = models.CharField("ქვეყანა", max_length=100, null=True, blank=True)
    postcode = models.IntegerField("საფოსტო კოდი", null=True, blank=True)
    mobile = models.CharField("ტელეფონის ნომერი", max_length=100, null=True, blank=True)

    last_active_datetime = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"
