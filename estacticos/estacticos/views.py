from django.shortcuts import render

def herencia (request):
    return render(request,'herencia.html') 

def ejemplo (request):
    return render(request,'ejemplo.html')

def otra (request):
    return render(request,'otra.html')