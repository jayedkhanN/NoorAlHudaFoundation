import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create initial admin user from environment variables"

    def handle(self, *args, **options):

        username = os.environ.get("INITIAL_ADMIN_USERNAME")
        email = os.environ.get("INITIAL_ADMIN_EMAIL")
        password = os.environ.get("INITIAL_ADMIN_PASSWORD")

        if not username or not email or not password:
            self.stdout.write(
                self.style.WARNING(
                    "Initial admin environment variables are not set."
                )
            )
            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "is_staff": True,
                "is_superuser": True,
            },
        )

        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Initial admin '{username}' created successfully."
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Initial admin '{username}' updated successfully."
                )
            )