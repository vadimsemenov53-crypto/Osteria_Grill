from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            email="admin@gmail.com",
            defaults={
                "is_active": True,
                "is_superuser": True,
                "is_staff": True,
            },
        )

        if created:
            user.set_password("7777")
            user.save()

            self.stdout.write(self.style.SUCCESS(f"Суперпользователь создан: {user.email}"))
        else:
            self.stdout.write(self.style.WARNING(f"Суперпользователь уже существует: {user.email}"))
