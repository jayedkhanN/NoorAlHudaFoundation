from django.shortcuts import render
from .models import ContactMessage
from volunteers.models import Volunteer
from donations.models import Donation


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


def about(request):
    return render(request, 'about.html')


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

    return render(request, "contact.html")
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def admin_dashboard(request):
    from volunteers.models import Volunteer
    from donations.models import Donation
    from .models import ContactMessage

    volunteer_count = Volunteer.objects.count()
    donation_count = Donation.objects.count()
    contact_count = ContactMessage.objects.count()

    total_amount = sum(
        donation.amount or 0
        for donation in Donation.objects.all()
    )

    return render(
        request,
        "admin_dashboard.html",
        {
            "volunteer_count": volunteer_count,
            "donation_count": donation_count,
            "contact_count": contact_count,
            "total_amount": total_amount,
        }
    )