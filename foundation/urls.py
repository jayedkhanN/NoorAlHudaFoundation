from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from home import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path(
        'volunteers/',
        include('volunteers.urls')
    ),

    path(
        'donate/',
        include('donations.urls')
    ),

    path(
        'dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    path(
        'api/',
        include('api.urls')
    ),

    path('api/auth/', include('userauth.urls')),
]


# Media files - development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )