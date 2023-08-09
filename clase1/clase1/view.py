from django.http import HttpResponse

    #La funciónes "saludo y desdpedida" devuelve una respuesta HTTP con el mensaje "¡Hola Mundo! y Adios Mundo"
    #return: un objeto HttpResponse con el mensaje "¡Hola Mundo! y Adios Mundo".

def saludo(request):
    return  HttpResponse("Hola Mundo!")

def despedida(request):
    return  HttpResponse("Adios Mundo!")

#ruta con parametro
# nos devuelve si es mayor o menor de edad de pendiendo del numero que pasamos como parametro
def adulto(request, edad):
    if edad >= 18:
        return  HttpResponse("eres mayor de edad!")
    else:
        return  HttpResponse(" eres menor de edad!")
