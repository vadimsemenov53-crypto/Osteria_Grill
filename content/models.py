from django.db import models

class ContentRestaurantAbout(models.Model):
    """ Модель для представления страницы 'О ресторане' (изменения - управления контентом). """

    # История ресторана
    image_history = models.ImageField(
        upload_to="content/history_rest",
        verbose_name="Фото для истории",
        help_text="Загрузите для истории ресторана",
    )

    history_title = models.CharField(
        max_length=500,
        verbose_name="Заголовок истории ресторана.",
        help_text="Введите заголовок для истории ресторана."
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
        help_text="Укажите заголовок для истории о Шеф-поваре",
    )

    chef_p1 = models.TextField(
        verbose_name="История шефа (видимое)",
        help_text="Введите историю шефа",
    )

    chef_p2 = models.TextField(
        verbose_name="История шефа (скрытое)",
        help_text="Введите историю шефа. Для нового абзаца оставьте пустую строку.",
    )

    class Meta:
        verbose_name = "Страница 'О ресторане'"

# <p class="lead text-body">
#     {{ content.chef_story|linebreaks }}
# </p>
