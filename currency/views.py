# from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Exchange


class ExchangeRatesListView(ListView):
    model = Exchange
    template_name = 'list_exchange_rates.html'
    context_object_name = 'exchanges_rates'

# def list_exchange_rates(request):
#     exchange_rates_list = Exchange.objects.all()
#     content = 'exchanges_rates'
#     return render(request, 'list_exchange_rates.html', {'exchanges_rates': exchange_rates_list})
