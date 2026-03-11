from django.db import models


class DriverModel(models.Model):
    fio = models.CharField(max_length=225)
    photo = models.ImageField(upload_to='Drivers_photos/')
    birth_date = models.DateField()
    car_choice = models.CharField(max_length=100)
    exprience = models.IntegerField()
    has_license = models.BooleanField(default=True)

