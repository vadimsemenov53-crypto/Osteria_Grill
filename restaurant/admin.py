from django.contrib import admin

from restaurant.models import Booking, ContactForm, RestaurantService, Table, RestaurantEmployee


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


@admin.register(RestaurantService)
class AdminRestaurantService(admin.ModelAdmin):
    """Админка управления - модель RestaurantService."""

    list_display = (
        "order",
        "name",
    )
    search_fields = ("name",)


@admin.register(ContactForm)
class AdminContactForm(admin.ModelAdmin):
    """Админка управления - модель ContactForm."""

    list_display = (
        "first_name",
        "last_name",
        "phone",
        "email",
    )
    ordering = (
        "first_name",
        "last_name",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
    )

@admin.register(RestaurantEmployee)
class AdminRestaurantEmployee(admin.ModelAdmin):
    """Админка управления - модель AdminRestaurantEmployee."""

    list_display = (
        "first_name",
        "last_name",
        "post",
    )

    ordering = (
        "post",
    )

    search_fields = (
        "first_name",
        "last_name",
    )