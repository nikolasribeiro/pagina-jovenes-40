from django.urls import path
from .views import home, detail_noticias

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>', detail_noticias, name="detalle-noticia")
]
