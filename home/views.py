from django.shortcuts import render
from django.views import View
from .models import Drink, Category, About
# Create your views here.


class HomeView(View):

    def get(self, request):
        cold_drinks = Drink.objects.filter(category=1)
        hot_drinks = Drink.objects.filter(category=2)
        fruit_drinks = Drink.objects.filter(category=3)
        special_drinks = Drink.objects.filter(category=4)
        about = About.objects.all().order_by('?')
        return render(request, 'home/index.html', {'cold_drinks': cold_drinks, 'hot_drinks': hot_drinks,
                                                   'fruit_drinks': fruit_drinks, 'special_drinks': special_drinks
                                                   , 'about': about})
