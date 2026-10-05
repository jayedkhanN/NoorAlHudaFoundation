from django.urls import path

from .views import (
    api_home,
    DonationListCreateAPIView,
    HelpRequestListCreateAPIView,
    VolunteerListCreateAPIView,
    EventListCreateAPIView,
    EventParticipationListCreateAPIView,
)


urlpatterns = [
    path(
        '',
        api_home,
        name='api_home',
    ),

    path(
        'donations/',
        DonationListCreateAPIView.as_view(),
        name='donation-list-create',
    ),

    path(
        'help-requests/',
        HelpRequestListCreateAPIView.as_view(),
        name='help-request-list-create',
    ),

    path(
        'volunteers/',
        VolunteerListCreateAPIView.as_view(),
        name='volunteer-list-create',
    ),

    path(
        'events/',
        EventListCreateAPIView.as_view(),
        name='event-list-create',
    ),

    path(
        'event-participations/',
        EventParticipationListCreateAPIView.as_view(),
        name='event-participation-list-create',
    ),
]