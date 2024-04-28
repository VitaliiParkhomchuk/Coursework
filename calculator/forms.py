from .models import Calculation
from django.forms import ModelForm, NumberInput, TextInput

class CalculationForm(ModelForm):
    class Meta:
        model = Calculation
        fields = {'area', 'tempNow', 'tempNeed', 'city'}

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
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City'
            })
        }