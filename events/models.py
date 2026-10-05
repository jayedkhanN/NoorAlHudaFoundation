from django.db import models


class Event(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    date = models.DateField()

    time = models.TimeField(
        blank=True,
        null=True
    )

    location = models.CharField(
        max_length=200
    )

    image = models.ImageField(
        upload_to='events/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

class EventParticipation(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='participations'
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"