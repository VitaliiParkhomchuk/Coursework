from django.shortcuts import render, redirect
from .models import Calculation
from .forms import CalculationForm

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

def result(request):
    obj = Calculation.objects.order_by('-id').first()
    test = obj.area+obj.tempNow
    res = obj.area + obj.tempNeed + obj.tempNow
    n1 = str(obj.area)
    n2 = str(obj.tempNow)
    n3 = str(obj.tempNeed)
    
    data = {
        'res':res
    }
    
    return render(request, 'calculator/result.html', {'data':data})
