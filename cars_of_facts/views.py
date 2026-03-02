from django.shortcuts import render, get_object_or_404
from .models import Car

# Эта функция выведет список всех машин (car_list.html)
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

# Эта функция выведет детали конкретной машины (car_detail.html)
def car_detail(request, pk):
    car = get_object_or_404(Car, id=pk)
    return render(request, 'car_detail.html', {'car': car})
