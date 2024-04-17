from django.shortcuts import render

def index(request):
    data={
        'area': 10,
        'temp': 15
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')