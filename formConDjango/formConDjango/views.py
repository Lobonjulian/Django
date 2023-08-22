from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ConctactForm

def form(request) :              #valores por defecto
    comment_form = CommentForm({'name': 'julian', 'url': 'www.google.com', 'comment': 'Comentario'})
    return render(request, 'form.html', {'comment_form' : comment_form})

def goal(request) :
    if request.method != 'POST':
        return HttpResponse('Metodo no permitido')
    
    return HttpResponse(request.POST['name'])

def widget(request) :
    if request.method == 'GET':
        form = ConctactForm()
        return render(request, 'widget.html', {'form' : form})

    if request.method == 'POST':
        form = ConctactForm(request.POST)
        if form.is_valid():
            return HttpResponse('Valido')
        else:
        # cuando los datos erroneos 
            return render(request, 'widget.html', {'form' : form})