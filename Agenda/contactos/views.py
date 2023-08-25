from django.shortcuts import render
from .models import Contacto
from .forms import ContactosForm
def index(request):
    # nos da todos los valores que este si no existe nos lo da en blanco
    contactos = Contacto.objects.filter(name__contains=request.GET.get('search', ''))
    
    context = {
        'contactos': contactos
    }
    return render(request, 'contactos/index.html', context)

def view(request, id):
    contacto = Contacto.objects.get(id=id)
    context = {
        'contacto': contacto
    }
    return render(request, 'contactos/details.html', context)

def edit(request, id):
    if(request.method == 'GET'):
        contacto = Contacto.objects.get(id=id)
        form = ContactosForm(instance = contacto)
        context = {
            'form': form
        }
    return render(request, 'contactos/create.html', context)