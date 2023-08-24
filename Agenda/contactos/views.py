from django.shortcuts import render
from .models import Contacto

def index(request):
    # nos da todos los valores que este si no existe nos lo da en blanco
    contactos = Contacto.objects.filter(name__contains=request.GET.get('search', ''))
    
    context = {
        'contactos': contactos
    }
    return render(request, 'contactos/index.html', context)