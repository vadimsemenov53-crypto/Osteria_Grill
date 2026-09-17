from django import forms

from restaurant.models import ContactForm, Booking


class ContactFormModelForm(forms.ModelForm):
    """ Форма модели - ContactForm (базовая валидация данных).  """
    class Meta:
        model = ContactForm
        fields = ["first_name", "last_name", "phone", "email"]


class BookingModelForm(forms.ModelForm):
    """ Форма модели - Booking (базовая валидация данных).  """
    class Meta:
        model = Booking
        fields = ["guests"]

    def clean_guests(self):
        """ Метод валидации данных ограничивающий выбор 0 количества гостей. """
        guests = self.cleaned_data["guests"]

        if guests < 1:
            raise forms.ValidationError(
                "Количество гостей должно быть не менее 1."
            )

        return guests
