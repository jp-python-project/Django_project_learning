from datetime import datetime, time, date
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.IntegerField()
    floor = models.IntegerField()

    def __str__(self):
        return f" {self.name} :{self.room_number} on floor {self.floor}"


class Meeting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    participants = models.ManyToManyField(get_user_model())

    def __str__(self):
        return f" {self.title} :{self.date} :{self.start_time} :{self.duration}"
