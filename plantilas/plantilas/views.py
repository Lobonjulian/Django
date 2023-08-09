from django.shortcuts import render

def simple(request):
    return render(request,'simple.html', {})

def dinamico(request,name):
    #retorno renderizado(requerimiento, plantilla, contexto)
    categorias = {'codigo','lola','sabroso'}
    
    contexto = {'name': name, 'categoria' : categorias}
    return render (request,'dinamico.html', contexto)

