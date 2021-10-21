from currency.views import ExchangeRatesListView

from django.urls import path


urlpatterns = [
    path('list_exchange_rates/', ExchangeRatesListView.as_view(), name='list-exchange-rates'),
]
