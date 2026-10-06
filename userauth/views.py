from rest_framework import generics, status
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail

import random

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, LoginSerializer
from .models import PasswordResetOTP


# =========================================================
# REGISTER
# =========================================================

class RegisterAPIView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# =========================================================
# LOGIN
# =========================================================

class LoginAPIView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            refresh = RefreshToken.for_user(user)

            return Response({

                'message': 'Login successful',

                'username': user.username,

                'email': user.email,

                'access': str(refresh.access_token),

                'refresh': str(refresh),

            }, status=status.HTTP_200_OK)

        return Response({

            'message': 'Invalid username or password'

        }, status=status.HTTP_401_UNAUTHORIZED)


# =========================================================
# FORGOT PASSWORD - SEND OTP
# =========================================================

class ForgotPasswordAPIView(generics.GenericAPIView):

    def post(self, request):

        username = request.data.get('username')

        if not username:
            return Response({
                'message': 'Username is required'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            return Response({
                'message': 'Username not found'
            }, status=status.HTTP_404_NOT_FOUND)

        if not user.email:
            return Response({
                'message':
                'No email address is registered for this account'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Generate 6 digit OTP
        otp = str(random.randint(100000, 999999))

        # Delete old OTPs
        PasswordResetOTP.objects.filter(
            user=user,
            is_verified=False
        ).delete()

        # Save new OTP
        PasswordResetOTP.objects.create(
            user=user,
            otp=otp
        )

        # Send OTP email
        try:

            send_mail(
                'Noor Al Huda - Password Reset OTP',

                f'''
Hello {user.username},

Your password reset OTP is:

{otp}

Please use this OTP to reset your password.

If you did not request a password reset,
please ignore this email.

Regards,
Noor Al Huda Foundation
''',

                None,

                [user.email],

                fail_silently=False,
            )

        except Exception as e:

            print("========== OTP EMAIL ERROR ==========")
            print(type(e).__name__)
            print(str(e))
            print("=====================================")

            return Response({

                'message':
                'Unable to send OTP email',

                'error':
                str(e)

            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({

            'message':
            'OTP sent to your registered email'

        }, status=status.HTTP_200_OK)


# =========================================================
# VERIFY OTP
# =========================================================

class VerifyOTPAPIView(generics.GenericAPIView):

    def post(self, request):

        username = request.data.get('username')

        otp_value = request.data.get('otp')

        if not username or not otp_value:

            return Response({

                'message':
                'Username and OTP are required'

            }, status=status.HTTP_400_BAD_REQUEST)

        try:

            user = User.objects.get(
                username=username
            )

        except User.DoesNotExist:

            return Response({

                'message':
                'Username not found'

            }, status=status.HTTP_404_NOT_FOUND)

        reset_otp = PasswordResetOTP.objects.filter(

            user=user,

            otp=otp_value,

            is_verified=False

        ).last()

        if reset_otp is None:

            return Response({

                'message':
                'Invalid OTP'

            }, status=status.HTTP_400_BAD_REQUEST)

        # Mark OTP as verified
        reset_otp.is_verified = True

        reset_otp.save()

        return Response({

            'message':
            'OTP verified successfully'

        }, status=status.HTTP_200_OK)


# =========================================================
# RESET PASSWORD
# =========================================================

class ResetPasswordAPIView(generics.GenericAPIView):

    def post(self, request):

        username = request.data.get('username')

        new_password = request.data.get(
            'new_password'
        )

        confirm_password = request.data.get(
            'confirm_password'
        )

        if not username:

            return Response({

                'message':
                'Username is required'

            }, status=status.HTTP_400_BAD_REQUEST)

        if not new_password:

            return Response({

                'message':
                'New password is required'

            }, status=status.HTTP_400_BAD_REQUEST)

        if not confirm_password:

            return Response({

                'message':
                'Confirm password is required'

            }, status=status.HTTP_400_BAD_REQUEST)

        if new_password != confirm_password:

            return Response({

                'message':
                'Passwords do not match'

            }, status=status.HTTP_400_BAD_REQUEST)

        if len(new_password) < 6:

            return Response({

                'message':
                'Password must be at least 6 characters'

            }, status=status.HTTP_400_BAD_REQUEST)

        try:

            user = User.objects.get(
                username=username
            )

        except User.DoesNotExist:

            return Response({

                'message':
                'Username not found'

            }, status=status.HTTP_404_NOT_FOUND)

        # Check whether OTP was verified
        verified_otp = PasswordResetOTP.objects.filter(

            user=user,

            is_verified=True

        ).last()

        if verified_otp is None:

            return Response({

                'message':
                'Please verify OTP first'

            }, status=status.HTTP_400_BAD_REQUEST)

        # Change password
        user.set_password(new_password)

        user.save()

        # Delete used OTP
        PasswordResetOTP.objects.filter(
            user=user
        ).delete()

        return Response({

            'message':
            'Password reset successfully'

        }, status=status.HTTP_200_OK)