from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=16)
    phone = PhoneNumberField(null=False, blank=True, unique=True, default=None)

    def clean(self):
        self.first_name = self.first_name.capitalize
        self.last_name = self.last_name.capitalize

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age} {self.phone}"
