from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm

def form(request) :              #valores por defecto
    comment_form = CommentForm({'name': 'julian', 'url': 'www.google.com', 'comment': 'Comentario'})
    return render(request, 'form.html', {'comment_form' : comment_form})

def goal(request) :
    if request.method != 'POST':
        return HttpResponse('Metodo no permitido')
    
    return HttpResponse(request.POST['name'])