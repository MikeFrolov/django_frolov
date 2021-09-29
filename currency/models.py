from django.db import models

from .choices import CURRENCIES


class Exchange(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    source = models.CharField(max_length=20, default='NoName')
    currency = models.CharField(max_length=4, choices=CURRENCIES)
    buy_price = models.DecimalField(max_digits=19, decimal_places=5)
    sale_price = models.DecimalField(max_digits=19, decimal_places=5)

    def __str__(self):
        return f"{self.create_at}: {self.source}, {self.currency}, BUY: {self.buy_price}; SALE: {self.sale_price};\n"
