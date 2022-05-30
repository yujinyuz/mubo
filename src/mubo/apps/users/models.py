from typing import Optional

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, password: Optional[str] = None, **kwargs):
        user = self.model(**kwargs)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        return user

    def create_superuser(self, password: str, **kwargs):
        user = self.create_user(password=password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(update_fields=["is_staff", "is_superuser"])
        return user


class User(AbstractUser):

    objects = UserManager()

    # override to extend the max length
    first_name = models.CharField(
        "first name",
        max_length=254,
        blank=True,
        db_index=True,
    )
    last_name = models.CharField("last name", max_length=254, blank=True, db_index=True)
    email = models.EmailField(verbose_name="email", unique=True)
    phone = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
