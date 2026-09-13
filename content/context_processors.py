from content.models import BaseContentRestaurant


def site_content(request):
    """Функция формирования общего контекста для бара навигации, футера, заднего фона."""
    content = BaseContentRestaurant.objects.get(id=1)

    return {
        "site_content": content,
    }
