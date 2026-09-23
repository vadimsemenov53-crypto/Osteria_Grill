from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class BaseContentRestaurant(models.Model):
    """Модель для представления общего контента: бар-навигации, футер, задний фон.
    (изменения - управления контентом)."""

    # Панель навигации
    logo = models.ImageField(
        upload_to="content/logo",
        verbose_name="Логотип",
        help_text="Загрузите логотип заведения.",
    )

    # Задний фон
    background_image = models.ImageField(
        upload_to="content/site",
        verbose_name="Фоновое изображение",
        help_text="Загрузите фоновое изображение заднего фона",
    )

    # Футер (левая часть)
    rest_name = models.CharField(
        max_length=250, verbose_name="Название заведения", help_text="Введите название заведения"
    )

    rest_title = models.TextField(
        verbose_name="Короткий заголовок", help_text="Введите небольшое и говорящее предложение о ресторане"
    )

    # Футер контактные данные

    address = models.CharField(max_length=250, verbose_name="Адрес", help_text="Введите адрес ресторана")

    phone = PhoneNumberField(
        verbose_name="Телефон",
        help_text="Введите номер телефона",
    )

    email = models.EmailField(verbose_name="Почта ресторана", help_text="Введите почту ресторана")

    def __str__(self):
        """Метод строкового представления - BaseContentRestaurant."""
        return "Общий контент сайта"

    class Meta:
        verbose_name = "Общий контент сайта"
        verbose_name_plural = "Общий контент сайта"


class ContentRestaurantHome(models.Model):
    """Модель для представления страницы 'Главная' (изменения - управления контентом)."""

    # Карточка о ресторане
    rest_image = models.ImageField(
        upload_to="content/main_rest",
        verbose_name="Фото для истории",
        help_text="Загрузите для истории ресторана",
    )
    rest_name = models.CharField(
        max_length=250,
        verbose_name="Название ресторана",
        help_text="Введите название ресторана",
    )

    rest_title = models.CharField(
        max_length=500,
        verbose_name="Короткое предисловие",
        help_text="Введите описывающее ресторан предисловие",
    )

    rest_description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание ресторана",
    )

    # Карточка шеф-повара
    chef_headline = models.CharField(
        max_length=250,
        verbose_name="Заголовок",
        help_text="Укажите заголовок карточки",
    )

    chef_history = models.TextField(
        verbose_name="Короткая история шеф-повара",
        help_text="Введите краткую историю",
    )

    chef_awards = models.TextField(
        verbose_name="Награды", help_text="Введите награды. Каждую указывайте с новой строки"
    )

    def __str__(self):
        """Метод строкового представления - ContentRestaurantHome."""
        return "Контент главной страницы."

    class Meta:
        """Метаданные модели ContentRestaurantHome."""

        verbose_name = "Страница 'Главная'"
        verbose_name_plural = "Страница 'Главная'"


class ContentRestaurantAbout(models.Model):
    """Модель для представления страницы 'О ресторане' (изменения - управления контентом)."""

    # История ресторана
    image_history = models.ImageField(
        upload_to="content/history_rest",
        verbose_name="Фото для истории",
        help_text="Загрузите для истории ресторана",
    )

    history_title = models.CharField(
        max_length=500,
        verbose_name="Заголовок истории ресторана.",
        help_text="Введите заголовок для истории ресторана.",
    )
    history_p1 = models.TextField(
        verbose_name="Первый пункт",
        help_text="Введите историю ресторана",
    )

    history_p2 = models.TextField(
        verbose_name="Второй пункт",
        help_text="Введите историю ресторана. Для нового абзаца оставьте пустую строку.",
        blank=True,
    )

    # История шефа
    chef_image = models.ImageField(
        upload_to="content/history_chef",
        verbose_name="Фото для Шеф-повара",
        help_text="Загрузите для истории Шеф-повара",
    )
    chef_title = models.CharField(
        max_length=500,
        verbose_name="Заголовок истории Шеф-повара",
        help_text="Введите заголовок для истории о Шеф-поваре",
    )

    chef_p1 = models.TextField(
        verbose_name="История шефа (видимое)",
        help_text="Введите историю шефа",
    )

    chef_p2 = models.TextField(
        verbose_name="История шефа (скрытое)",
        help_text="Введите историю шефа. Для нового абзаца оставьте пустую строку.",
    )

    # Миссия
    mission_title = models.CharField(
        max_length=250,
        verbose_name="Заголовок миссии",
        help_text="Введите заголовок для миссии",
    )

    mission = models.TextField(
        verbose_name="Миссия",
        help_text="Введите основное содержание (миссию).",
    )

    # Ценности
    value_title = models.CharField(
        verbose_name="Заголовок ценностей",
        help_text="Введите заголовок ценностей",
    )

    values = models.TextField(
        verbose_name="Ценности ресторана",
        help_text="Каждую ценность указывайте с новой строки",
    )

    def __str__(self):
        """Метод строкового представления - ContentRestaurantAbout."""
        return "Контент страницы 'О ресторане'."

    class Meta:
        """Метаданные модели ContentRestaurantAbout."""

        verbose_name = "Страница 'О ресторане'"
        verbose_name_plural = "Страница 'О ресторане'"
