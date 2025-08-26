from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Flight
from .forms import FlightForm

# Create your views here.

def home(request):
    # Zona de inicio
    return render(request, 'flights/home.html')

def flight_create(request):
    # Registrar vuelos
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flights:list')
    else:
        form = FlightForm()
    return render(request, 'flights/create.html', {'form': form})

def flight_list(request):
    # Listar vuelos
    flights = Flight.objects.order_by('price')
    return render(request, 'flights/list.html', {'flights': flights})

def flight_stats(request):
    # Estadisticas de vuelos
    n_nacionales      = Flight.objects.filter(ftype='N').count()
    n_internacionales = Flight.objects.filter(ftype='I').count()
    avg_nacionales    = Flight.objects.filter(ftype='N').aggregate(
        avg=Avg('price')
    )['avg']
    return render(request, 'flights/stats.html', {
        'n_nacionales': n_nacionales,
        'n_internacionales': n_internacionales,
        'avg_nacionales': avg_nacionales,
    })
