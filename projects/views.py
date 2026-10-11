
from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .models import Project


@require_GET
def projects_count(request):
    count = Project.objects.count()

    return JsonResponse({
        "projects_count": count
    })

