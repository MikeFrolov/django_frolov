from django.db import models
from django.utils import timezone


class ContactUs(models.Model):
    sent_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    message = models.TextField()
    email_from = models.CharField(max_length=100)
    email_to = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sent_date},{self.title}, {self.message}, {self.email_from}, {self.email_to}"
