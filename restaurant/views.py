from django.shortcuts import render
from django.views.generic import ListView, View

from restaurant.models import Table, Booking


class HomeView(View):
    """ Контроллер главной страницы. """
    template_name = 'home.html'

    def get(self, request):
        """ Метод для рендеринга главной страницы. """
        return render(request, self.template_name)