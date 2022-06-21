from django.db import models

from core.models import TimeStampModel

class User(TimeStampModel):
    name         = models.CharField(max_length=45)
    account      = models.CharField(max_length=128, unique=True)
    email        = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=45, unique=True)
    password     = models.CharField(max_length=500)
    point        = models.CharField(max_length=100, default="100000")

    class Meta:
        db_table = "users"