from django import forms
from django.contrib.auth.forms import AuthenticationForm


class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-switch'
            else:
                field.widget.attrs['class'] = 'form-control'

class UserLoginForm(StyleFromMixin, AuthenticationForm):
    pass