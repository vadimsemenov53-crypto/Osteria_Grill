from django.contrib.auth.views import LoginView
from users.forms import UserLoginForm


class UserLogin(LoginView):
    """ Контроллер для аутентификации пользователей. """
    template_name = "login.html"
    form_class = UserLoginForm