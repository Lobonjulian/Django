from asyncio.windows_events import NULL
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacto
from .forms import ContactosForm

def index(request, letter = NULL ):
    if letter != NULL:
        contactos = Contacto.objects.filter(name__istartswith=letter)
    else:
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
    contacto = Contacto.objects.get(id=id)
        
    if(request.method == 'GET'):
        form = ContactosForm(instance = contacto)
        context = {
            'form': form,
            'id': id        
        }
        return render(request, 'contactos/edit.html', context)
    
    if(request.method == 'POST'):
        form = ContactosForm(request.POST, instance = contacto)
        if form.is_valid():
            form.save()
        context = {
            'form': form,
            'id': id
        }
        messages.success(request, 'Contacto actualizado')
        return render(request, 'contactos/edit.html', context) 
    
def create(request):
    if(request.method == 'GET'):
        form = ContactosForm()
        context = {
            'form': form
        }
        return render(request, 'contactos/create.html', context)
    
    if request.method == 'POST':
        form =  ContactosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contactos')
    
def delete(request, id):
    contacto = Contacto.objects.get(id=id)
    contacto.delete()
    return redirect('contactos')