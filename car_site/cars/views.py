from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.
def add(request):
    if request.method == 'POST':
        brand = request.POST['brand']
        year = request.POST['year']
        models.Car.objects.create(brand=brand, year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')

def delete(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
        except:
            print('pk not found!')
        finally:
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html')

def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars': all_cars}

    return render(request, 'cars/list.html', context=context)
