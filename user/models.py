from django.db import models

from django.contrib.auth.models import AbstractUser,Permission, UserManager


class User(AbstractUser):
    is_driver_user = models.BooleanField(default=False)
    is_normal_user = models.BooleanField(default=False)
    is_admin_user = models.BooleanField(default=False)
    

