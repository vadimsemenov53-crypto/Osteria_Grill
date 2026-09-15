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
        ordering = ("number",)


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


class RestaurantService(models.Model):
    """Модель для представления услуг ресторана."""

    name = models.CharField(
        max_length=250,
        verbose_name="Название",
        help_text="Укажите название услуги",
    )
    description = models.TextField(verbose_name="Описание", help_text="Укажите описание услуги.")

    order = models.PositiveIntegerField(
        unique=True,
        default=0,
        verbose_name="Порядок отображения",
        help_text="Чем меньше число, тем выше услуга в списке",
    )

    def __str__(self):
        """Метод строкового представления - RestaurantService."""
        return self.name

    class Meta:
        verbose_name = "Услуга ресторана"
        verbose_name_plural = "Услуги ресторана"
        ordering = ["order", "name"]


class ContactForm(models.Model):
    """Модель для представления формы обратной связи."""

    first_name = models.CharField(max_length=100, verbose_name="Имя", help_text="Введите имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", help_text="Введите фамилию")
    phone = models.CharField(unique=True, max_length=100, verbose_name="Телефон", help_text="Введите номер телефона")
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Укажите почту", blank=True)

    def __str__(self):
        """Метод строкового представления - ContactForm."""
        return f"{self.first_name} {self.last_name}"

    class Meta:
        """Метаданные модели ContactForm"""

        verbose_name = "контакт обратной связи"
        verbose_name_plural = "контакты обратной связи"
        ordering = [
            "first_name",
            "last_name",
        ]


class RestaurantEmployee(models.Model):
    """Модель для представления сотрудника ресторана."""

    class Position(models.TextChoices):
        """Подкласс RestaurantEmployee - представление должностей."""

        CLEANER = "cleaner", "Уборщица"
        WAITER = "waiter", "Официант"
        BARTENDER = "bartender", "Бармен"
        COOK = "cook", "Повар"
        HEAD_CHEF = "head_chef", "Шеф-повар"
        DIRECTOR = "director", "Директор"
        ADMINISTRATOR = "administrator", "Администратор"

    photo = models.ImageField(
        upload_to="restaurant/photo_employee",
        verbose_name="Фото",
        help_text="Загрузите фото сотрудника",
        blank=True,
        null=True,
    )
    first_name = models.CharField(max_length=100, verbose_name="Имя", help_text="Введите имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия", help_text="Введите фамилию")
    post = models.CharField(
        choices=Position.choices,
        max_length=100,
        verbose_name="Должность",
        help_text="Укажите должность",
        null=True,
        blank=True,
    )
    work_experience = models.PositiveIntegerField(
        verbose_name="Опыт",
        help_text="Укажите опыт работы (лет)",
        null=True,
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Порядок отображения",
        help_text="Чем меньше число, тем выше сотрудник в списке",
    )

    def __str__(self):
        """Метод строкового представления - RestaurantEmployee."""
        return f"{self.post} - {self.last_name}"

    class Meta:
        """Метаданные модели RestaurantEmployee."""

        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = [
            "order",
            "last_name",
        ]
