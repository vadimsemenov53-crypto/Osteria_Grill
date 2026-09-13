from django.contrib import admin

from content.models import ContentRestaurantAbout


@admin.register(ContentRestaurantAbout)
class AdminContentRestaurantAbout(admin.ModelAdmin):
    """Админка управления - модель ContentRestaurantAbout.
    (управление контентом страницы 'о ресторане')"""

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
