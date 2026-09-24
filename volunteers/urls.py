from django.urls import path
from . import views

urlpatterns = [
    path('', views.volunteer_list, name='volunteer_list'),

    path(
        'register/',
        views.volunteer_register,
        name='volunteer_register'
    ),

    path(
        'edit/<int:id>/',
        views.volunteer_edit,
        name='volunteer_edit'
    ),

    path(
        'delete/<int:id>/',
        views.volunteer_delete,
        name='volunteer_delete'
    ),
]