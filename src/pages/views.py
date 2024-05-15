from django.shortcuts import HttpResponse, render, Http404
from django.views.decorators.gzip import gzip_page

from menu.models import RegularPizza, SicilianPizza

# Create your views here.

@gzip_page
def index(request):
    context = {
        "reg_pizza": RegularPizza.objects.all(),
        "sic_pizza": SicilianPizza.objects.all()
    }
    return render(request, 'pages/index.html', context)
