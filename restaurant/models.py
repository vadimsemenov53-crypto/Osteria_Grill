from django.conf import settings
from django.db import models


class Table(models.Model):
    """Модель для представления стола в ресторане."""

    CAT_VIP = "VIP"
    CAT_STANDARD = "standard"

    CAT_CHOICES = [
        (CAT_VIP, "Премиум"),
        (CAT_STANDARD, "Стандарт"),
    ]

    number = models.PositiveIntegerField(unique=True, verbose_name="Номер стола", help_text="Укажите номер стола")

    capacity = models.PositiveIntegerField(
        verbose_name="Количество мест",
        help_text="Максимальное количество гостей",
    )
    category = models.CharField(
        choices=CAT_CHOICES,
        max_length=25,
        verbose_name="Категория",
        help_text="Укажите категорию стола",
    )

    def __str__(self):
        """Метод строкового представления - Table."""
        return f"Стол №{self.number} - {self.capacity} чел/мест ({self.category})"

    class Meta:
        """Метаданные модели - Table."""

        verbose_name = "Стол"
        verbose_name_plural = "Столы"


class Booking(models.Model):
    """Модель представления бронирования."""

    class Status(models.TextChoices):
        """Подкласс Booking - представление статусов бронирования."""

        PENDING = "pending", "Ожидает подтверждения"
        CONFIRMED = "confirmed", "Подтверждено"
        CANCELLED = "cancelled", "Отменено"
        COMPLETED = "completed", "Завершено"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Посетитель",
        help_text="Укажите посетителя",
        related_name="bookings",
    )

    table = models.ForeignKey(
        Table,
        on_delete=models.PROTECT,
        verbose_name="Стол",
        help_text="Укажите стол",
        related_name="bookings",
    )

    start_at = models.DateTimeField(
        verbose_name="Время начала бронирования", help_text="Укажите время начала бронирования"
    )

    end_at = models.DateTimeField(
        verbose_name="Время окончания бронирования",
        help_text="Укажите время окончания бронирования",
    )

    guests = models.PositiveIntegerField(
        verbose_name="Количество гостей",
        help_text="Укажите количество гостей",
    )

    status = models.CharField(
        max_length=25,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="Статус",
        help_text="Укажите статус бронирования",
    )

    comment = models.TextField(verbose_name="Комментарий", help_text="Укажите комментарий", blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    def __str__(self):
        """Метод строкового представления - Booking."""
        return f"{self.user} - Стол №{self.table.number}"

    class Meta:
        """Метаданные модели - Booking."""

        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
        ordering = [
            "-created_at",
        ]
