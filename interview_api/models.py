from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


from interview_api.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)
    is_candidate = models.BooleanField(default=True)
    is_interviewer = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = UserManager()
