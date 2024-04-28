from django.db import models

class Calculation(models.Model):
    area = models.FloatField('Площа')  
    tempNow = models.FloatField('Наявна температура')
    tempNeed = models.FloatField('Потрібна температура')
    city = models.CharField('Місто', max_length=250, default='Рівне')

    
    
    class Meta:
        verbose_name = 'Обрахунок'
        verbose_name_plural = 'Обрахунки'
       
