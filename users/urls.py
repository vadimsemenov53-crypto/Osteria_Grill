from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserLogin

app_name = UsersConfig.name

urlpatterns = [
    path("login/", UserLogin.as_view(next_page="restaurant:home"), name="login"),
    path("logout/", LogoutView.as_view(next_page="restaurant:home"), name="logout"),
]
