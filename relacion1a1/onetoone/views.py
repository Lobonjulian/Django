from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurante

def create(request):
    place = Place(name="Lugar 1", addres="Calle Demo")
    place.save()
    
    restaurante = Restaurante(place=place, number_of_employees=8)
    restaurante.save()
    
    return HttpResponse(restaurante.place.name)