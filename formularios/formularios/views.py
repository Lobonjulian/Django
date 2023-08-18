from django.shortcuts import render
from django.http import HttpResponse

def getform(request):
    return render(request,'form.html',{})

def getgoal(request):
    if request.method != 'GET':
        return HttpResponse('el POST no esta Soportado por esta ruta')

    name = request.GET['name']
    return render(request,'succes.html', {'name': name})

def postform(request):
    return render(request, 'postform.html', {})

def postgoal(request):
    #estrctura de guarda
        if request.method != 'POST':
            return HttpResponse('el GET no esta Soportado por esta ruta')
        
        info = request.POST['info']
        return render(request, 'postsucces.html', {'info' : info})
    
