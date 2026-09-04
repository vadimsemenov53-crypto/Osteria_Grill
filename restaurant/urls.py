from django.urls import path
from restaurant.apps import RestaurantConfig
from restaurant.views import HomeView

app_name = RestaurantConfig.name

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]
