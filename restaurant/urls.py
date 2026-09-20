from django.urls import path

from restaurant.apps import RestaurantConfig
from restaurant.views import BookingView, HomeView, RestaurantAboutView, booking_verification, BookingListView

app_name = RestaurantConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("about/", RestaurantAboutView.as_view(), name="about"),
    path("booking", BookingView.as_view(), name="booking"),
    path("booking-confirm/<str:token>/", booking_verification, name="booking-confirm"),
    path("booking_list", BookingListView.as_view(), name="booking_list"),
]
