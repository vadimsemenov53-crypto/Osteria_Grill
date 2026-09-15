from django.urls import path

from restaurant.apps import RestaurantConfig
from restaurant.views import BookingView, HomeView, RestaurantAboutView

app_name = RestaurantConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("about/", RestaurantAboutView.as_view(), name="about"),
    path("booking", BookingView.as_view(), name="booking"),
]
