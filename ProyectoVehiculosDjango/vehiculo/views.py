from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

@permission_required('vehiculo.add_vehiculomodel', raise_exception=True)
def agregar_vehiculo(request):
    form = VehiculoForm()
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    
    return render(request, 'add.html', {'form': form})

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'add.html'
    success_url = reverse_lazy('index.html')

# @login_required
# def listar_vehiculos(request):
#     vehiculos = Vehiculo.objects.all()
#     return render(request, 'listar.html', {'vehiculos': vehiculos})

@login_required
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    vehiculos_con_condicion = []
    for vehiculo in vehiculos:
        if vehiculo.precio < 10000:
            condicion_precio = 'Bajo'
        elif 10000 <= vehiculo.precio <= 30000:
            condicion_precio = 'Medio'
        else:
            condicion_precio = 'Alto'

        vehiculos_con_condicion.append({
            'vehiculo': vehiculo,
            'condicion_precio': condicion_precio
        })
    
    context = {'vehiculos_con_condicion': vehiculos_con_condicion}
    return render(request, 'listar.html', context)