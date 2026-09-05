from django.shortcuts import render
from django.views.generic import View

from restaurant.models import RestaurantService


class HomeView(View):
    """ Контроллер главной страницы. """
    template_name = 'home.html'

    def get(self, request):
        """ Метод для рендеринга главной страницы. """
        services = RestaurantService.objects.all()

        context = {
            "services" : services,
        }

        return render(request, self.template_name, context=context)