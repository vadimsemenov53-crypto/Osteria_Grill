from django.core.management import call_command
from django.core.management.base import BaseCommand

from content.models import BaseContentRestaurant, ContentRestaurantAbout, ContentRestaurantHome
from restaurant.models import ContactForm, RestaurantEmployee, RestaurantService, Table


class Command(BaseCommand):
    help = "Загрузка начальных данных из фикстуры."

    def handle(self, *args, **options):
        self.stdout.write("Удаление начальных данных...")
        BaseContentRestaurant.objects.all().delete()
        ContentRestaurantHome.objects.all().delete()
        ContentRestaurantAbout.objects.all().delete()

        Table.objects.all().delete()
        RestaurantService.objects.all().delete()
        ContactForm.objects.all().delete()
        RestaurantEmployee.objects.all().delete()

        self.stdout.write(self.style.SUCCESS("Начальные данные удалены."))

        try:
            call_command("loaddata", "start_fixtures.json")

            self.stdout.write(self.style.SUCCESS("Фикстуры успешно загружены."))

        except Exception as error:
            self.stdout.write(self.style.ERROR(f"При загрузке фикстур произошла ошибка: {error}"))
