from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from User.managers import UserManager
from . import constants as user_constants


class User(AbstractUser):
    
    username = None
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    sen = models.PositiveIntegerField(default=1)
    codemeli = models.CharField(max_length=50, unique=True)
    telephone = models.CharField(max_length=50)
    noe_tadris = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.PositiveSmallIntegerField(
        choices=user_constants.USER_TYPE_CHOICES
    )

    REQUIRED_FIELDS = ["name","address","telephone","user_type","sen"]
    USERNAME_FIELD = "codemeli"

    objects = UserManager()