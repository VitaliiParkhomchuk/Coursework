from .models import Calculation
from django.forms import ModelForm, NumberInput

class CalculationForm(ModelForm):
    class Meta:
        model = Calculation
        fields = {'area', 'tempNow', 'tempNeed'}

        widgets = {
            'area': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Area'
            }),
            'tempNow': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'TempNow'
            }),
            'tempNeed': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'TempNeed'
            })
        }