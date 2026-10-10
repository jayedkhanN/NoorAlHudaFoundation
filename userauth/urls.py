
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    RegisterAPIView,
    LoginAPIView,
    ForgotPasswordAPIView,
    VerifyOTPAPIView,
    ResetPasswordAPIView,
)


urlpatterns = [
    path(
        'register/',
        RegisterAPIView.as_view(),
        name='register'
    ),

    path(
        'login/',
        LoginAPIView.as_view(),
        name='login'
    ),

    path(
        'forgot-password/',
        ForgotPasswordAPIView.as_view(),
        name='forgot-password'
    ),

    path(
        'verify-otp/',
        VerifyOTPAPIView.as_view(),
        name='verify-otp'
    ),

    path(
        'reset-password/',
        ResetPasswordAPIView.as_view(),
        name='reset-password'
    ),

    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
