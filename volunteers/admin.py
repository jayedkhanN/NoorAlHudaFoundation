from django.contrib import admin
from .models import Volunteer


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'volunteer_area',
        'availability',
        'created_at',
    )

    list_filter = (
        'volunteer_area',
        'availability',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'phone',
        'address',
    )