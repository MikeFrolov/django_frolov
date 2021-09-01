from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=23)
    phone = PhoneNumberField(null=False, blank=True, unique=True, default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age} {self.phone}"
