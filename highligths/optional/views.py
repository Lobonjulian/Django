from django.shortcuts import render

def optional(request, id=0):
    return render(request, 'optional.html', {'id': id})
