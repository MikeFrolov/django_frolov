from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=16)


class Group(models.Model):
    group_name = models.CharField(max_length=60)  # faculty abbreviation + year of start education
    faculty_name = models.CharField(max_length=200)  # List of disciplines from
    # https://www.educationindex.ru/articles/archive/all/polnyy-spisok-predmetnyh-distciplin-prepodavaemyh-v-vuzah-britanii-24/
    nos = models.IntegerField(default=20)  # nos = number of students


class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    discipline = models.CharField(max_length=200)
