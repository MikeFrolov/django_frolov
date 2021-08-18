from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=60)
    faculty_name = models.CharField(max_length=200)
    number_of_students = models.IntegerField(default=20)

    def __str__(self):
        return f"{self.group_name} {self.faculty_name} {self.number_of_students}"
