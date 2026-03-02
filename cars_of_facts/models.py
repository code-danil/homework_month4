from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Car(models.Model):
    name_car = models.CharField(max_length=100, verbose_name='укажите название машин')
    brand_model = models.CharField(max_length=100, verbose_name='укажите название модели')
    year = models.IntegerField(validators=[MinValueValidator(1886), MaxValueValidator(2025)], verbose_name='год выпуска')
    color = models.CharField(max_length=30, verbose_name='укажите название цвета', blank=True)
    engine_volume = models.FloatField(verbose_name='укажите обьем двигателя')
    description = models.TextField(verbose_name='укажите описание машин', null=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену' , default=0)
    image = models.ImageField(upload_to='cars/',  verbose_name='укажите облаку')
    fuel_type = models.CharField(max_length=20, verbose_name='укжите тип топлива', default='Бензин')
    country = models.CharField(max_length=100)



    def __str__(self):
        return f'{self.brand_model} ({self.year})'
    
