from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    discipline = models.CharField(max_length=200)