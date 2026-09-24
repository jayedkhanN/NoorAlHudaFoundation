from django.shortcuts import render, redirect
from .models import Donation
from decimal import Decimal


def donate(request):

    if request.method == "POST":

        donor_name = request.POST.get("donor_name", "").strip()

        amount_text = request.POST.get("amount", "").strip()

        transaction_id = request.POST.get("transaction_id", "").strip()

        message = request.POST.get("message", "").strip()

        # Amount optional
        if amount_text:
            amount = Decimal(amount_text)
        else:
            amount = None

        Donation.objects.create(
            donor_name=donor_name,
            amount=amount,
            transaction_id=transaction_id,
            message=message
        )

        return redirect("donate_success")

    return render(request, "donations/donate.html")


def donate_success(request):

    return render(
        request,
        "donations/donate_success.html"
    )