from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Модель представления пользователя."""

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Введите адрес эл.почты")
    phone = PhoneNumberField(
        verbose_name="Телефон",
        blank=True,
        help_text="Введите номер телефона",
    )

    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        blank=True,
        null=True,
    )

    token = models.CharField(max_length=100, verbose_name="Token", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
