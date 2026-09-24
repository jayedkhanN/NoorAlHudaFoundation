from django.contrib import admin
from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):

    list_display = (
        'donor_name',
        'amount',
        'transaction_id',
        'status',
        'created_at',
    )

    search_fields = (
        'donor_name',
        'transaction_id',
        'message',
    )

    list_filter = (
        'status',
        'created_at',
    )