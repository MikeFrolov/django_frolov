from currency.views import list_exchange_rates

from django.urls import path


urlpatterns = [
    path('list_exchange_rates/', list_exchange_rates, name='list-exchange-rates'),
]
