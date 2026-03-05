from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Tour(models.Model):
    title = models.CharField(max_length=200, verbose_name='название тура')
    description = models.TextField(verbose_name='описание')
    caterories = models.ManyToManyField(Category, related_name='tours')

    def __str__(self):
        return self.title
    

class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='Review')
    author = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f'Отзыа от {self.author} на {self.tour}'
    

class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username} записан на {self.tour}'