from django.shortcuts import render
from django.contrib import messages

def message(request):
    messages.success(request, 'Mensaje de éxito')
    return render(request, 'messages.html', {})