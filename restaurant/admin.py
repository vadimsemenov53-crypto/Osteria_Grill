from django.contrib import admin

from restaurant.models import Booking, Table


@admin.register(Table)
class AdminTable(admin.ModelAdmin):
    """Админка управления - модель Table."""

    list_display = (
        "number",
        "capacity",
        "category",
    )
    list_filter = ("category",)


@admin.register(Booking)
class AdminBooking(admin.ModelAdmin):
    """Админка управления - модель Booking."""

    list_display = (
        "user",
        "table",
        "start_at",
        "end_at",
        "guests",
        "status",
    )
    list_filter = (
        "status",
        "created_at",
    )
    search_fields = ("user__email",)
