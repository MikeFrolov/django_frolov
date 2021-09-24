from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=40)
    discipline = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.group_name} {self.discipline}"
