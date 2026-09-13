from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View

from restaurant.forms import ContactFormModelForm
from restaurant.models import RestaurantEmployee, RestaurantService

from content.models import ContentRestaurantAbout


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

        return render(request, self.template_name, context)

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


class RestaurantAboutView(View):
    """Контроллер для представления страницы о ресторане."""

    template_name = "rest_about.html"

    def get(self, request):
        """Метод для рендеринга страницы 'о ресторане'."""
        employees = RestaurantEmployee.objects.exclude(photo="").order_by("order")
        content = ContentRestaurantAbout.objects.get(id=1)

        context = {
            "employees": employees,
            "content": content,
        }
        return render(request, self.template_name, context)
