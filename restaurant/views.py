from datetime import datetime, timedelta

from django.contrib import messages
from django.shortcuts import get_object_or_404, render
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

            table = get_object_or_404(Table, id=table_id)

            booking_date = form.cleaned_data["booking_date"]
            booking_time = form.cleaned_data["booking_time"]

            start_at = datetime.combine(booking_date, booking_time)
            start_at = timezone.make_aware(start_at)
            end_at = start_at + timedelta(hours=2)

            booking_comment = request.POST.get("bookingComment")

            booking.user = request.user
            booking.table = table
            booking.start_at = start_at
            booking.end_at = end_at
            booking.status = Booking.Status.PENDING
            booking.comment = booking_comment

            booking.save()

        context = {
            "tables": tables,
            "form": form,
            "selected_table_id": table_id,
        }

        return render(request, self.template_name, context)
