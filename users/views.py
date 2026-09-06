import secrets

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from users.forms import UserLoginForm, UserRegisterForm
from users.models import User


class UserLoginView(LoginView):
    """Контроллер для аутентификации пользователей."""

    template_name = "login.html"
    form_class = UserLoginForm


class UserCreateView(CreateView):
    """Контроллер создания пользователя."""

    model = User
    template_name = "user_form.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        token = secrets.token_hex(16)
        user.token = token
        user.save()

        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"

        send_mail(
            subject="OSTERIA GRILL Подтверждение почты",
            message=f"Здравствуйте, перейди по ссылке для подтверждения почты: {url}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        messages.success(
            self.request,
            f"Регистрация успешно завершена! " f"Мы отправили письмо для подтверждения на {user.email}.",
        )

        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = None
    user.save()

    send_mail(
        subject="Добро пожаловать в OSTERIA GRILL",
        message="Спасибо за регистрацию! Теперь вам доступны бронирование столов онлайн, сервис доставки, оплата онлайн.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
    )

    return redirect(reverse("users:login"))
