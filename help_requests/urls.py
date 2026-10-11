
from django.urls import path
from . import views

urlpatterns = [
    path(
        "families-helped-count/",
        views.families_helped_count,
        name="families_helped_count",
    ),
]
