from django.urls import path

from currency.views import list_exchange_rates


urlpatterns = [
    path('list_exchange_rates/', list_exchange_rates, name='list-exchange-rates'),
]
