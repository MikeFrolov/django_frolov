from celery import shared_task

import requests

from .models import Exchange
# from .choices import CURRENCIES


"""@shared_task
def get_currency_rates_privat():
    # Parser of PrivatBank currencies
    exchange_response_privat = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11')

    exchange_result_privat = exchange_response_privat.json()
    for rate_privat in exchange_result_privat:

        if rate_privat.get('ccy') not in CURRENCIES:
            continue

        exchange = Exchange(
            source='PrivatBank',
            currency=rate_privat.get('ccy', 'NNC'),  # NNC - No Name Currency
            buy_price=rate_privat.get('buy'),
            sale_price=rate_privat.get('sale')
        )
        exchange.save()

    return f'Exchange rates from PrivatBank have been successfully recorded!'"""


@shared_task
def get_currency_rates_mono():
    exchange_response_mono = requests.get('https://api.monobank.ua/bank/currency')

    exchange_result_mono = exchange_response_mono.json()
    currency_codes = {840: "USD", 978: "EUR"}

    for rate_mono in exchange_result_mono:
        currency_code = rate_mono.get('currencyCodeA', )

        if currency_code not in currency_codes.keys() or rate_mono.get('currencyCodeB', ) in currency_codes.keys():
            continue

        currency = currency_codes[currency_code]
        exchange = Exchange(
            source='MonoBank',
            currency=currency,
            buy_price=rate_mono.get('rateBuy', ),
            sale_price=rate_mono.get('rateSell', )
        )
        exchange.save()

    return 'Exchange rates from MonoBank have been successfully recorded!'


@shared_task
def get_currency_rates_nats():
    exchange_response_nats = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')

    exchange_result_nats = exchange_response_nats.json()
    currency_codes = (840, 978)
    for rate_nats in exchange_result_nats:

        if rate_nats.get('r030', ) not in currency_codes:
            continue

        exchange = Exchange(
            source='NationalBank',
            currency=rate_nats.get('cc', ),
            buy_price=rate_nats.get('rate', ),
            sale_price=rate_nats.get('rate', )
        )
        exchange.save()

    return 'Exchange rates from NationalBank have been successfully recorded!'
