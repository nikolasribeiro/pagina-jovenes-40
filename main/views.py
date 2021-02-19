from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    fechas = []
    
    # Verificador que le dira a Django en caso de que no existan fechas importantes
    # que imprima por pantalla un parrafo con la leyenda: "No hay fechas importantes para este mes"
    verificador = True

    # Obtenemos las fechas importantes
    mes_model  = FechasImportantes.objects.first()
    raw_fechas = FechasImportantes.objects.values_list('fecha1', flat=True)

    # Traemos las fechas desde un TextField para evitar crear 31 campos de texto
    if len(raw_fechas) >= 1 and raw_fechas[0] is not "":
        verificador = True
        for fechas_model in raw_fechas[0].split('\n'):
            fechas.append(fechas_model)
    else:
        verificador = False

    # Obtenemos las noticias
    noticias = Noticias.objects.all().order_by('-fecha')


    # Contexto
    context = {
        "fechas":fechas,
        "verificador":verificador,
        "mes":mes_model,
        "noticias":noticias
    }

    return render(request, 'main/index.html', context)