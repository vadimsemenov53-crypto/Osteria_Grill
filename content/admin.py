from django.contrib import admin

from content.models import BaseContentRestaurant, ContentRestaurantAbout, ContentRestaurantHome


@admin.register(BaseContentRestaurant)
class AdminBaseContentRestaurant(admin.ModelAdmin):
    """Админка управления - модель BaseContentRestaurant.
    (управление-изменение: бар-навигации, футер, задний фон)."""

    fieldsets = (
        (
            "Бар навигации",
            {"fields": ("logo",)},
        ),
        (
            "Задний фон",
            {"fields": ("background_image",)},
        ),
        (
            "Футер (левая часть)",
            {
                "fields": (
                    "rest_name",
                    "rest_title",
                )
            },
        ),
        (
            "Футер контактные данные",
            {
                "fields": (
                    "address",
                    "phone",
                    "email",
                )
            },
        ),
    )

    def has_add_permission(self, request):
        """Запрещаем создавать больше одной записи."""
        return not ContentRestaurantAbout.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Запрещаем удалять единственную запись контента."""
        return False


@admin.register(ContentRestaurantHome)
class AdminContentRestaurantHome(admin.ModelAdmin):
    """Админка управления - модель ContentRestaurantAbout.
    (управление контентом страницы 'Главная')."""

    fieldsets = (
        (
            "Карточка ресторана",
            {
                "fields": (
                    "rest_image",
                    "rest_name",
                    "rest_title",
                    "rest_description",
                )
            },
        ),
        (
            "Карточка шеф-повара",
            {
                "fields": (
                    "chef_headline",
                    "chef_history",
                    "chef_awards",
                )
            },
        ),
    )

    def has_add_permission(self, request):
        """Запрещаем создавать больше одной записи."""
        return not ContentRestaurantAbout.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Запрещаем удалять единственную запись контента."""
        return False


@admin.register(ContentRestaurantAbout)
class AdminContentRestaurantAbout(admin.ModelAdmin):
    """Админка управления - модель ContentRestaurantAbout.
    (управление контентом страницы 'о ресторане')."""

    fieldsets = (
        (
            "История ресторана",
            {
                "fields": (
                    "image_history",
                    "history_title",
                    "history_p1",
                    "history_p2",
                )
            },
        ),
        (
            "История шефа",
            {
                "fields": (
                    "chef_image",
                    "chef_title",
                    "chef_p1",
                    "chef_p2",
                )
            },
        ),
        (
            "Миссия",
            {
                "fields": (
                    "mission_title",
                    "mission",
                )
            },
        ),
        (
            "Ценности",
            {
                "fields": (
                    "value_title",
                    "values",
                )
            },
        ),
    )

    def has_add_permission(self, request):
        """Запрещаем создавать больше одной записи."""
        return not ContentRestaurantAbout.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Запрещаем удалять единственную запись контента."""
        return False
