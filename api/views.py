from django.http import JsonResponse

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from donations.models import Donation
from help_requests.models import HelpRequest
from volunteers.models import Volunteer
from events.models import Event, EventParticipation

from .serializers import (
    DonationSerializer,
    HelpRequestSerializer,
    VolunteerSerializer,
    EventSerializer,
    EventParticipationSerializer,
)


def api_home(request):

    return JsonResponse({
        "message": "Noor Al Huda Foundation API is working!",
        "status": "success"
    })


class DonationListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Donation.objects.filter(
            user=self.request.user
        ).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class HelpRequestListCreateAPIView(
    generics.ListCreateAPIView
):
    serializer_class = HelpRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HelpRequest.objects.filter(
            user=self.request.user
        ).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class VolunteerListCreateAPIView(generics.ListCreateAPIView):

    queryset = Volunteer.objects.all().order_by("-created_at")
    serializer_class = VolunteerSerializer


class EventListCreateAPIView(generics.ListCreateAPIView):

    queryset = Event.objects.all().order_by("date", "time")
    serializer_class = EventSerializer


class EventParticipationListCreateAPIView(generics.ListCreateAPIView):

    queryset = EventParticipation.objects.all().order_by("-created_at")
    serializer_class = EventParticipationSerializer