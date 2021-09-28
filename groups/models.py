from django.db import models

from students.models import Student

from teachers.models import Teacher


class Group(models.Model):
    group_name = models.CharField(max_length=40, unique=True)
    discipline = models.CharField(max_length=40)
    curator = models.ForeignKey(Teacher, null=True, default=None, blank=True, on_delete=models.PROTECT)
    headman = models.ForeignKey(Student, null=True, default=None, blank=True, on_delete=models.CASCADE)
    students = models.ManyToManyField(
        Student,
        related_name="students_in_group",
        default=None,
        blank=True,
        max_length=10
    )

    def students_list(self):
        return ", \n".join([str(s) for s in self.students.all()])

    def __str__(self):
        return self.group_name
