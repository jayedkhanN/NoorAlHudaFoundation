
from django.urls import path
from . import views

urlpatterns = [
    path(
        "count/",
        views.projects_count,
        name="projects_count",
    ),
]
