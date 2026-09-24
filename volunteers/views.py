from django.shortcuts import render, redirect, get_object_or_404
from .models import Volunteer
from .forms import VolunteerForm


def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(
        request,
        "volunteer_list.html",
        {"volunteers": volunteers}
    )


def volunteer_register(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("volunteer_list")

    else:
        form = VolunteerForm()

    return render(
        request,
        "volunteer_form.html",
        {"form": form}
    )


def volunteer_edit(request, id):
    volunteer = get_object_or_404(Volunteer, id=id)

    if request.method == "POST":
        form = VolunteerForm(request.POST, instance=volunteer)

        if form.is_valid():
            form.save()
            return redirect("volunteer_list")

    else:
        form = VolunteerForm(instance=volunteer)

    return render(
        request,
        "volunteer_form.html",
        {"form": form}
    )


def volunteer_delete(request, id):
    volunteer = get_object_or_404(Volunteer, id=id)

    if request.method == "POST":
        volunteer.delete()
        return redirect("volunteer_list")

    return render(
        request,
        "volunteer_confirm_delete.html",
        {"volunteer": volunteer}
    )