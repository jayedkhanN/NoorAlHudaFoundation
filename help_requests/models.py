from django.db import models
from django.contrib.auth.models import User


class HelpRequest(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="help_requests",
        null=True,
        blank=True
    )

    CATEGORY_CHOICES = [
        ("Food Support", "Food Support"),
        ("Medical Support", "Medical Support"),
        ("Education Support", "Education Support"),
        ("Financial Support", "Financial Support"),
        ("Emergency Support", "Emergency Support"),
        ("Other", "Other"),
    ]

    full_name = models.CharField(
        max_length=100
    )

    phone_number = models.CharField(
        max_length=20
    )

    address = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Approved", "Approved"),
            ("Rejected", "Rejected"),
        ],
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name