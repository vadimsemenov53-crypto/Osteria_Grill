from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class StyleFromMixin:
    """Класс миксин для стилизации форм."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-switch"
            else:
                field.widget.attrs["class"] = "form-control"


class UserLoginForm(StyleFromMixin, AuthenticationForm):
    """Форма стилизации UserLoginView."""

    pass


class UserRegisterForm(StyleFromMixin, UserCreationForm):
    """Форма стилизации UserCreateView."""

    class Meta:
        model = User
        fields = ("email", "phone", "password1", "password2")
