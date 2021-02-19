from django.shortcuts import render
from .models import Galeria
# Create your views here.

def galeria(request):
    imagenes = Galeria.objects.all()
    context = {
        "imagenes":imagenes
    }
    
    return render(request, 'galeria/galeria.html', context)