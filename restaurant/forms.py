from datetime import datetime, timedelta

from django import forms
from django.utils import timezone

from restaurant.booking_validation import BookingValidationMixin
from restaurant.models import Booking, ContactForm


class BookingUpdateForm(BookingValidationMixin, forms.ModelForm):
    """Форма модели - Booking (обновление данных)."""

    booking_date = forms.DateField(
        label="Дата бронирования",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
            }
        ),
    )

    booking_time = forms.ChoiceField(
        label="Время бронирования",
        choices=[
            ("12:00", "12:00"),
            ("14:00", "14:00"),
            ("16:00", "16:00"),
            ("18:00", "18:00"),
            ("20:00", "20:00"),
            ("22:00", "22:00"),
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        """Инициализация полей booking_date, booking_time"""
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            local_start = timezone.localtime(self.instance.start_at)

            self.fields["booking_date"].initial = local_start.date()
            self.fields["booking_time"].initial = local_start.time()

    def save(self, commit=True):
        """Сохраняет изменённые дату и время бронирования."""
        booking = super().save(commit=False)

        booking_date = self.cleaned_data["booking_date"]
        booking_time = datetime.strptime(
            self.cleaned_data["booking_time"],
            "%H:%M",
        ).time()

        start_at = datetime.combine(
            booking_date,
            booking_time,
        )

        start_at = timezone.make_aware(start_at)

        booking.start_at = start_at
        booking.end_at = start_at + timedelta(hours=2)

        if commit:
            booking.save()

        return booking

    class Meta:
        model = Booking
        fields = ["table", "booking_date", "booking_time", "guests", "comment"]

        widgets = {
            "guests": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                }
            ),
            "table": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),
        }


class ContactFormModelForm(forms.ModelForm):
    """Форма модели - ContactForm (базовая валидация данных)."""

    class Meta:
        model = ContactForm
        fields = ["first_name", "last_name", "phone", "email"]


class BookingModelForm(BookingValidationMixin, forms.ModelForm):
    """Форма модели - Booking (валидация данных)."""

    booking_date = forms.DateField(
        label="Дата бронирования",
        widget=forms.DateInput(
            attrs={
                "type": "date",
            }
        ),
    )

    booking_time = forms.ChoiceField(
        label="Время бронирования",
        choices=[
            ("12:00", "12:00"),
            ("14:00", "14:00"),
            ("16:00", "16:00"),
            ("18:00", "18:00"),
            ("20:00", "20:00"),
            ("22:00", "22:00"),
        ],
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Booking
        fields = ["table", "guests", "booking_date", "booking_time", "comment"]
