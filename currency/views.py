from django.shortcuts import render

from .models import Exchange


def list_exchange_rates(request):
    exchange_rates_list = Exchange.objects.all()
    return render(request, 'list_exchange_rates.html', {'exchanges_rates': exchange_rates_list})
