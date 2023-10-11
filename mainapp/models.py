from django.db import models


class School(models.Model):
    name = models.CharField(max_length=127)
    number = models.PositiveIntegerField(default=1)
    address = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    name = models.CharField(max_length=127)
    room_number = models.PositiveIntegerField(default=1)
    school = models.ForeignKey(
        to=School, on_delete=models.CASCADE
    )
    def __str__(self):
        return f'Class{self.name} - {self.school.name}'