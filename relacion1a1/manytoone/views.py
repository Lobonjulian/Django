from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulo, Reportero
from datetime import date


def create(request):
    reportero = Reportero(primer_nombre="Julian",apellido="Lobon", email="julitolos@example.com" )
    reportero.save()
    
    artculo1 = Articulo(headline="lorem ipum 1", pub_date=date(2023,8,16), reportero=reportero )
    artculo1.save()
    artculo2 = Articulo(headline="lorem ipum 2 ", pub_date=date(2013,10,6), reportero=reportero )
    artculo2.save()
    artculo3 = Articulo(headline="lorem ipum 3", pub_date=date(2023,5,26), reportero=reportero )
    artculo3.save()
    artculo4 = Articulo(headline="lorem ipum 4", pub_date=date(2023,3,30), reportero=reportero )
    artculo4.save()
    
    #resultado = artculo1.reportero.primer_nombre
    resultado = reportero.articulo_set.all()
    
    return HttpResponse(resultado)