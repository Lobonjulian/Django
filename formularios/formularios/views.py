from django.shortcuts import render
from django.http import HttpResponse

def form(request):
    return render(request,'form.html',{})

def goal(request):
    if request.method != 'GET':
        return HttpResponse('el POST no esta Soportadopor esta ruta')

    name = request.GET['name']
    return render(request,'succes.html', {'name': name})