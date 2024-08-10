from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    vin = models.CharField(max_length=20, unique=True)
    patente = models.CharField(max_length=6)
    numero_motor = models.CharField(max_length=20)
    cilindrada = models.CharField(max_length=10)
    anno = models.IntegerField()
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    version = models.CharField(max_length=20)

    def __str__(self):
        return f"Vin: {self.vin},  Patente: {self.patente})"
	
	