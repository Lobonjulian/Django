from django.shortcuts import render
from django.http import HttpResponse
from .models import Publicacion, Articulo


def create (request):
    articulo1 = Articulo(headline = 'articulo 1')
    articulo1.save()
    articulo2 = Articulo(headline = 'articulo 2')
    articulo2.save()
    articulo3 = Articulo(headline = 'articulo 3')
    articulo3.save()
    
    pub1 = Publicacion(titulo = 'publicacion 1')
    pub1.save()
    pub2 = Publicacion(titulo = 'publicacion 2')
    pub2.save()
    pub3 = Publicacion(titulo = 'publicacion 3')
    pub3.save()
    pub4 = Publicacion(titulo = 'publicacion 4')
    pub4.save()
    pub5 = Publicacion(titulo = 'publicacion 5')
    pub5.save()
    pub6 = Publicacion(titulo = 'publicacion 6')
    pub6.save()
    
    #relacion entre articulo y publicaciones
    articulo1.publicacion.add(pub1)
    articulo1.publicacion.add(pub3)
    articulo1.publicacion.add(pub4)
    articulo2.publicacion.add(pub6)
    articulo2.publicacion.add(pub5)
    articulo3.publicacion.add(pub2)
    
    #articulo3.publicacion.remove(pub1)
    
    resultado = articulo1.publicacion.all()
    
    
    return HttpResponse(resultado)