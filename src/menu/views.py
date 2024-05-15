from django.shortcuts import render
from .models import RegularPizza, SicilianPizza

def menu(request):
    most_popular_pizzas = RegularPizza.objects.filter(name__in=[
        'Mish-Mash Pizza', 'Pig in Paradise Pizza', 'Vegan Harvest Pizza',
        'Mushroom Cloud Pizza', 'Lekker\'izza Pizza'
    ])
    pizzas = RegularPizza.objects.all()
    return render(request, 'menu.html', {'most_popular_pizzas': most_popular_pizzas, 'pizzas': pizzas})
