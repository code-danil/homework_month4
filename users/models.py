from django.db import models


class ITSpecialist(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField()
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    specialization = models.CharField(max_length=50)
    experience = models.PositiveIntegerField()
    position = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    skills = models.TextField()
    salary = models.IntegerField()
    about = models.TextField()



