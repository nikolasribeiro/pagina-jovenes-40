from django.shortcuts import render, redirect
from .models import DatosObtenidos
from .forms import DatosObtenidosForm




# Create your views here.
def militancia(request):
    form = DatosObtenidosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    context = {
        "form":form
    }
    return render(request, 'militancia/militancia.html', context)