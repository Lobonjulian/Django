from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse('Funciona coretamente')

def create(request):
    #comment = Comment(name = 'julian',score = 5 , comment = 'este es un comentario')
    #comment.save()
    comment = Comment.objects.create(name='carlos')
    return HttpResponse('Ruta para probar crear objetos')

def delete(request):
    #comment = Comment.objects.get(id=1)
    #comment.delete()
    Comment.objects.get(id=2).delete()
    #Comment.objects.all().delete()
    return HttpResponse('Ruta para probar los objetos borrar ')