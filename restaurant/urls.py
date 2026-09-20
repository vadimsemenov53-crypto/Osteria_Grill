from django.urls import path

from restaurant.apps import RestaurantConfig
from restaurant.views import (BookingCancelView, BookingListView, BookingUpdateView, BookingView, HomeView,
                              RestaurantAboutView, booking_verification)

app_name = RestaurantConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("about/", RestaurantAboutView.as_view(), name="about"),
    path("booking/", BookingView.as_view(), name="booking"),
    path("booking-confirm/<str:token>/", booking_verification, name="booking-confirm"),
    path("booking_list/", BookingListView.as_view(), name="booking_list"),
    path("booking_update/<int:pk>/update/", BookingUpdateView.as_view(), name="booking_update"),
    path("booking_cancel/<int:pk>/", BookingCancelView.as_view(), name="booking_cancel"),
]
