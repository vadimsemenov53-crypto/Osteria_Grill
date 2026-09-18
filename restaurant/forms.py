from django import forms
from django.utils import timezone

from restaurant.models import Booking, ContactForm


class ContactFormModelForm(forms.ModelForm):
    """Форма модели - ContactForm (базовая валидация данных)."""

    class Meta:
        model = ContactForm
        fields = ["first_name", "last_name", "phone", "email"]


class BookingModelForm(forms.ModelForm):
    """Форма модели - Booking (валидация данных)."""

    booking_date = forms.DateField(
        label="Дата бронирования",
        widget=forms.DateInput(
            attrs={
                "type": "date",
            }
        ),
    )

    booking_time = forms.TimeField(
        label="Время бронирования",
        widget=forms.TimeInput(
            attrs={
                "type": "time",
            }
        ),
    )

    class Meta:
        model = Booking
        fields = ["guests", "booking_date", "booking_time"]

    def clean_guests(self):
        """Метод валидации данных ограничивающий выбор 0 количества гостей."""
        guests = self.cleaned_data["guests"]

        if guests < 1:
            raise forms.ValidationError("Количество гостей должно быть не менее 1.")

        return guests

    def clean_booking_date(self):
        """Метод валидации данных ограничивающий выбор прошедшую дату."""
        booking_date = self.cleaned_data["booking_date"]

        if booking_date < timezone.localdate():
            raise forms.ValidationError("Нельзя забронировать стол на прошедшую дату.")

        return booking_date
