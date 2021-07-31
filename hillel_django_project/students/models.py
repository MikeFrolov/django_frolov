from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=16)


class Group(models.Model):
    group_name = models.CharField(max_length=60)  # specialty abbreviation
    faculty_name = models.CharField(max_length=200)
    nos = models.IntegerField(default=2)  # nos = number of students




