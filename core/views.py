from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehiculo
from .forms import VehiculoForms
from django.db.models import Q
from django.contrib import messages
from rest_framework import viewsets
from .serializers import VehiculoSerializer

# Create your views here.

class VehiculoViewset(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

    def get_queryset(self):
        vehicle = Vehiculo.objects.all()

        plate = self.request.GET.get('patente')
        vin = self.request.GET.get('vin')

        if plate:
            vehicle = vehicle.filter(patente__contains=plate)
        elif vin :
            vehicle = vehicle.filter(vin__contains=vin)
        
        return vehicle


def home(request):
    
    return render(request, 'core/home.html')

def vehicles(request):
    search_query = request.GET.get('search', '')

    if search_query:
        vehiculos = Vehiculo.objects.filter(Q(patente__icontains=search_query) | Q(vin__icontains=search_query))
    else:
        vehiculos = Vehiculo.objects.all()

    data = {
        'vehiculos' : vehiculos
    }
    return render(request, 'core/vehicles.html', data)

def vehicle(request):
    data = {
        'form': VehiculoForms()
    }

    if request.method == 'POST':
        formulario = VehiculoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Vehículo agregado correctamente")
            return redirect(to="vehicles")
        else:
            data["form"] = formulario

    return render(request, 'core/vehicle.html', data)


def detail(request, id):

    vehiculo = get_object_or_404(Vehiculo, id=id)

    data = {
        'vehiculo': vehiculo
    }

    return render(request, 'core/detail.html', data)

