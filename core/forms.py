from django import forms
from .models import Vehiculo

class VehiculoForms(forms.ModelForm):
    patente = forms.CharField(widget=forms.TextInput(attrs={'class':'vehiculo-form-field', 'placeholder': 'Patente'}), label="")
    vin = forms.CharField(widget=forms.TextInput(attrs={'class':'vehiculo-form-field', 'placeholder': 'VIN'}), label="")
    numero_motor = forms.CharField(widget=forms.TextInput(attrs={'class':'vehiculo-form-field', 'placeholder': 'Número de Motor'}), label="")
    cilindrada = forms.CharField(widget=forms.TextInput(attrs={'class':'vehiculo-form-field', 'placeholder': 'Cilindrada'}), label="")
    anno = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'vehiculo-form-field', 'placeholder': 'Año'}), label="")
    marca = forms.CharField(widget=forms.TextInput(attrs={'class':'vehiculo-form-field', 'placeholder': 'Marca'}), label="")
    modelo = forms.CharField(widget=forms.TextInput(attrs={'class':'vehiculo-form-field', 'placeholder': 'Modelo'}), label="")
    version = forms.CharField(widget=forms.TextInput(attrs={'class':'vehiculo-form-field', 'placeholder': 'Versión'}), label="")

    class Meta:
        model = Vehiculo
        fields = '__all__'