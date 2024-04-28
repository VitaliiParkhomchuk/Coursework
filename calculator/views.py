from django.shortcuts import render, redirect
from .models import Calculation
from .forms import CalculationForm

from asgiref.sync import async_to_sync


import python_weather
import asyncio
import os

def calculator(request):
    data = Calculation.objects.all()
    return render(request, 'calculator/calculator.html', {'data': data})

def calculation(request):
    error = ''
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('result')
        else:
            error = 'Error'    

    form = CalculationForm()

    data = {
        'form':form,
        'error':error
    }
    return render(request, 'calculator/calculation.html', data)

@async_to_sync
async def get_weather_time_temperature(city):
    async with python_weather.Client() as client:
        weather = await client.get(city)
        time_temperature_list = []

        for daily in weather.daily_forecasts:
            for hourly in daily.hourly_forecasts:
                time_temperature_list.append((hourly.time.hour, hourly.temperature))

        return time_temperature_list


def result(request):
    obj = Calculation.objects.order_by('-id').first()
    res = obj.area + obj.tempNeed + obj.tempNow
    city = str(obj.city)
    weatherForecast = get_weather_time_temperature(city)
    
    data = {
        'city':city,
        'res':res,
        'weatherForecast':weatherForecast
    }
    
    return render(request, 'calculator/result.html', {'data':data})
