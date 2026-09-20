import secrets
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import View

from content.models import ContentRestaurantAbout, ContentRestaurantHome
from restaurant.forms import BookingModelForm, ContactFormModelForm
from restaurant.models import Booking, RestaurantEmployee, RestaurantService, Table


class HomeView(View):
    """Контроллер главной страницы."""

    template_name = "home.html"

    def get(self, request):
        """Метод для рендеринга главной страницы."""
        services = RestaurantService.objects.all()
        form = ContactFormModelForm()
        content = ContentRestaurantHome.objects.get(id=1)

        context = {
            "services": services,
            "form": form,
            "content": content,
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


class BookingView(View):
    """Контроллер для представления страницы бронирования."""

    template_name = "booking.html"

    def get(self, request):
        """Метод для рендеринга страницы 'бронирования'."""

        tables = Table.objects.all()
        form = BookingModelForm()

        context = {
            "tables": tables,
            "form": form,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        """Метод обработки POST - запросов бронирования."""
        tables = Table.objects.all()
        form = BookingModelForm(request.POST)

        table_id = request.POST.get("table")

        if form.is_valid():
            booking = form.save(commit=False)

            booking_date = form.cleaned_data["booking_date"]
            booking_time = form.cleaned_data["booking_time"]

            start_at = datetime.combine(booking_date, booking_time)
            start_at = timezone.make_aware(start_at)
            end_at = start_at + timedelta(hours=2)

            booking.user = request.user
            booking.start_at = start_at
            booking.end_at = end_at
            booking.status = Booking.Status.PENDING

            token = secrets.token_hex(16)
            booking.token = token

            booking.save()

            messages.success(
                request,
                f"""Спасибо! Мы получили вашу заявку на бронирование стола №{booking.table.number}.
                Перейдите на почту для подтверждения бронирования.""",
            )

            host = self.request.get_host()
            url = f"http://{host}/users/email-confirm/{token}/"

            send_mail(
                subject="OSTERIA GRILL Подтверждение бронирования",
                message=f"Здравствуйте, ваша заявка на бронирование.\n"
                f"Стол №{booking.table.number}, {booking.guests} человек.\n"
                f"C {booking.start_at} до {booking.end_at}.\n"
                f"Перейди по ссылке для подтверждения бронирования стола: {url}\n",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[booking.user.email],
            )

        context = {
            "tables": tables,
            "form": form,
            "selected_table_id": table_id,
        }

        return render(request, self.template_name, context)
