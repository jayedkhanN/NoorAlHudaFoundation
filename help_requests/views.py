
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .models import HelpRequest


@require_GET
def families_helped_count(request):
    """
    Count unique families whose help requests
    have been marked as Completed.
    """
    count = (
        HelpRequest.objects
        .filter(status="Completed")
        .values("address")
        .distinct()
        .count()
    )

    return JsonResponse({
        "families_helped": count
    })
