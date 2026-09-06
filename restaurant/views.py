from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import View

from restaurant.forms import ContactFormModelForm
from restaurant.models import ContactForm, RestaurantService


class HomeView(View):
    """Контроллер главной страницы."""

    template_name = "home.html"

    def get(self, request):
        """Метод для рендеринга главной страницы."""
        services = RestaurantService.objects.all()
        form = ContactFormModelForm()

        context = {
            "services": services,
            "form": form,
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        form = ContactFormModelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Спасибо! Мы получили ваше сообщение и обязательно свяжемся с вами.")

        services = RestaurantService.objects.all()

        context = {
            "services": services,
            "form": form,
        }

        return render(request, self.template_name, context)
