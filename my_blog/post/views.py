from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse

def update(request):
    author = Author.objects.get(id=1)
    author.name = 'julian'
    author.email = 'julian@example.com'
    author.save()
    return HttpResponse('Ruta para probar actualizar objetos')

# Consulta en base de datos atraves de objetos .
def queries(request):
    #obtener todos los elementos de un objeto
    authors = Author.objects.all()
    
    #obtener datos por filtro 
    filtrado = Author.objects.filter(email='edward69@example.net')
    
    #obtener un unico datos por filtrado
    author = Author.objects.get(id=24)
    
    #Limites de las consultas para solo n elementos
    limits = Author.objects.all()[:11]
    
    #obtener 10 valor saltando los 5 primeros
    offser = Author.objects.all()[5:10]
    
    #obtener todos los metodos ordenados 
    order = Author.objects.all().order_by('email')
    
    #obtener todos los metodos cuyo id sea menor a 17
    filter = Author.objects.filter(id__lte=17)
    
    #obtener todos los valores que contienen la palabra yes 
    yes = Author.objects.filter(name__contains='yes')
    
    
    return render(request, 'post/queries.html', {'authors': authors, 'filtrado': filtrado, 'author': author, 'limits' : limits, 'offser' : offser, 
                                                'order' : order, 'filter' : filter, 'yest' : yes })