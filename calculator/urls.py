from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calculator, name='calculator'),
    path('calculation', views.calculation, name='calculation'),
    path('result', views.result, name='result')
 ]