from django.contrib import admin
from .models import Event, EventParticipation


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'time',
        'location',
        'created_at',
    )

    list_filter = (
        'date',
        'location',
        'created_at',
    )

    search_fields = (
        'title',
        'location',
        'description',
    )


@admin.register(EventParticipation)
class EventParticipationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'event',
        'phone',
        'email',
        'created_at',
    )

    list_filter = (
        'event',
        'created_at',
    )

    search_fields = (
        'name',
        'phone',
        'email',
        'event__title',
    )