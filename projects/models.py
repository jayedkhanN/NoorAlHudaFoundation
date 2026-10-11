
from django.db import models


class Project(models.Model):
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Completed", "Completed"),
        ("Upcoming", "Upcoming"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
