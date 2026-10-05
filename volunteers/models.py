from django.db import models
from django.utils import timezone


class Volunteer(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=15
    )

    address = models.TextField()

    volunteer_area = models.CharField(
        max_length=100,
        blank=True,
        default=''
    )

    availability = models.CharField(
        max_length=100,
        blank=True,
        default=''
    )

    message = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.name