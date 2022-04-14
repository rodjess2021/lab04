from csv import list_dialects
from django.shortcuts import render
from multiprocessing import context
from select import select
from .models import Region, Candidato
# Create your views here.

def index(request):
    lista_regiones = Region.objects.all()
    context = {
        'lista_regiones': lista_regiones
    }
    return render(request, 'index.html', context)

def list_candidatos(request, region_id):
    lista_candidatos = Candidato.objects.filter(region=region_id)
    context = {
        'lista_candidatos': lista_candidatos
    }
    return render(request, 'candidatos.html', context)