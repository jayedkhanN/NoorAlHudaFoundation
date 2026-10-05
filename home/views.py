from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from .models import ContactMessage
from volunteers.models import Volunteer
from donations.models import Donation
from help_requests.models import HelpRequest
from events.models import Event, EventParticipation


# =========================================================
# HOME PAGE
# =========================================================

def home(request):

    volunteer_count = Volunteer.objects.count()
    donation_count = Donation.objects.count()

    total_amount = sum(
        donation.amount or 0
        for donation in Donation.objects.all()
    )

    return render(
        request,
        "index.html",
        {
            "volunteer_count": volunteer_count,
            "donation_count": donation_count,
            "total_amount": total_amount,
        }
    )


# =========================================================
# ABOUT PAGE
# =========================================================

def about(request):

    return render(
        request,
        "about.html"
    )


# =========================================================
# CONTACT PAGE
# =========================================================

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(
            request,
            "contact.html",
            {
                "success": "Your message has been sent successfully!"
            }
        )

    return render(
        request,
        "contact.html"
    )


# =========================================================
# ADMIN DASHBOARD
# =========================================================

@staff_member_required
def admin_dashboard(request):

    # =====================================================
    # DASHBOARD COUNTS
    # =====================================================

    volunteer_count = Volunteer.objects.count()

    donation_count = Donation.objects.count()

    help_request_count = HelpRequest.objects.count()

    event_count = Event.objects.count()

    participation_count = EventParticipation.objects.count()

    contact_count = ContactMessage.objects.count()


    # =====================================================
    # PENDING COUNTS
    # =====================================================

    pending_help_requests = HelpRequest.objects.filter(
        status="Pending"
    ).count()

    pending_donations = Donation.objects.filter(
        status="Pending"
    ).count()


    # =====================================================
    # TOTAL DONATION AMOUNT
    # =====================================================

    total_amount = sum(
        donation.amount or 0
        for donation in Donation.objects.all()
    )


    # =====================================================
    # TOTAL RECORDS
    # =====================================================

    total_records = (
        volunteer_count
        + donation_count
        + help_request_count
        + event_count
        + participation_count
        + contact_count
    )


    # =====================================================
    # CHART DATA
    # =====================================================

    chart_data = {

        "donations": donation_count,

        "help_requests": help_request_count,

        "volunteers": volunteer_count,

        "events": event_count,

        "participants": participation_count,

        "contacts": contact_count,
    }


    # =====================================================
    # RECENT DONATIONS
    # =====================================================

    recent_donations = Donation.objects.order_by(
        "-created_at"
    )[:5]


    # =====================================================
    # RECENT HELP REQUESTS
    # =====================================================

    recent_help_requests = HelpRequest.objects.order_by(
        "-created_at"
    )[:5]


    # =====================================================
    # RECENT VOLUNTEERS
    # =====================================================

    recent_volunteers = Volunteer.objects.order_by(
        "-created_at"
    )[:5]


    # =====================================================
    # RECENT EVENT PARTICIPATIONS
    # =====================================================

    recent_participations = EventParticipation.objects.select_related(
        "event"
    ).order_by(
        "-created_at"
    )[:5]


    # =====================================================
    # SEND DATA TO DASHBOARD
    # =====================================================

    return render(
        request,
        "admin_dashboard.html",
        {

            # -------------------------------------------------
            # Dashboard Counts
            # -------------------------------------------------

            "volunteer_count": volunteer_count,

            "donation_count": donation_count,

            "help_request_count": help_request_count,

            "event_count": event_count,

            "participation_count": participation_count,

            "contact_count": contact_count,


            # -------------------------------------------------
            # Pending Counts
            # -------------------------------------------------

            "pending_help_requests": pending_help_requests,

            "pending_donations": pending_donations,


            # -------------------------------------------------
            # Donation
            # -------------------------------------------------

            "total_amount": total_amount,


            # -------------------------------------------------
            # Total Records
            # -------------------------------------------------

            "total_records": total_records,


            # -------------------------------------------------
            # Chart Data
            # -------------------------------------------------

            "chart_data": chart_data,


            # -------------------------------------------------
            # Recent Activities
            # -------------------------------------------------

            "recent_donations": recent_donations,

            "recent_help_requests": recent_help_requests,

            "recent_volunteers": recent_volunteers,

            "recent_participations": recent_participations,
        }
    )