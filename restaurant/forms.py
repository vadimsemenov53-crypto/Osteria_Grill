from django import forms

from restaurant.models import ContactForm


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ["first_name", "last_name", "phone", "email"]
