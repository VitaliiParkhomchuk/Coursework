from django.db import models

class Calculation(models.Model):
    area = models.FloatField('Площа')  
    tempNow = models.FloatField('Наявна температура')
    tempNeed = models.FloatField('Потрібна температура')

    def __str__(self):
        return self.area
    
    class Meta:
        verbose_name = 'Обрахунок'
        verbose_name_plural = 'Обрахунки'
       
