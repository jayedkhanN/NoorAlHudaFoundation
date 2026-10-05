from rest_framework import serializers

from donations.models import Donation
from help_requests.models import HelpRequest
from volunteers.models import Volunteer
from events.models import Event, EventParticipation


class DonationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donation

        fields = [
            'id',
            'donor_name',
            'amount',
            'transaction_id',
            'message',
            'status',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'status',
            'created_at',
        ]


class HelpRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = HelpRequest

        fields = [
            'id',
            'full_name',
            'phone_number',
            'address',
            'category',
            'description',
            'status',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'status',
            'created_at',
        ]


class VolunteerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Volunteer

        fields = [
            'id',
            'name',
            'email',
            'phone',
            'address',
            'volunteer_area',
            'availability',
            'message',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
        ]


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event

        fields = [
            'id',
            'title',
            'description',
            'date',
            'time',
            'location',
            'image',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
        ]


class EventParticipationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventParticipation

        fields = [
            'id',
            'event',
            'name',
            'phone',
            'email',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
        ]