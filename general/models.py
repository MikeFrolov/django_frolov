from django.db import models


class Logger(models.Model):
    objects = None
    method = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    execution_time = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    """def __str__(self):
        return f'{self.method} {self.path} {self.execution_time} {self.created}'"""
