from django.db import models


class Donation(models.Model):

    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='donations'
    )

    donor_name = models.CharField(
        max_length=100,
        blank=True
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True
    )

    message = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Verified", "Verified"),
            ("Rejected", "Rejected"),
        ],
        default="Pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.donor_name or "Anonymous Donation"