from django.db import models
from django.contrib.auth.models import AbstractUser
from djangoessentials.models import TimeBasedStampModel


class User(TimeBasedStampModel):
    email = models.EmailField(("Email Address"), unique=True)
    phone = models.CharField((""), max_length=15, blank=True, null=True)
    balance = models.DecimalField(
        ("Balance"), max_digits=10, decimal_places=2, default=0.0
    )
    reputation_score = models.FloatField(default=0.0)
    is_seller = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
