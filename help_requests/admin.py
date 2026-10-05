from django.contrib import admin
from .models import HelpRequest


@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'full_name',
        'phone_number',
        'category',
        'status',
        'created_at',
    )

    list_filter = (
        'category',
        'status',
        'created_at',
    )

    search_fields = (
        'user__username',
        'full_name',
        'phone_number',
        'address',
    )