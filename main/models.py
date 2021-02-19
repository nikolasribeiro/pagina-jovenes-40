from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Noticias(models.Model):
    titulo = models.CharField(
        verbose_name="Titulo de la noticia", 
        max_length=150, 
        default=""
    )

    descripcion = models.TextField(
        verbose_name="Descripcion de la noticia",
        default=""
    )

    imagen = models.ImageField(upload_to="static/img/main")

    autor   = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        default=""
    )

    fecha = models.DateTimeField(
        verbose_name="Fecha de publicacion", 
        auto_now=False,
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo

class FechasImportantes(models.Model):
    nombre = models.CharField(
        verbose_name="Nombre del mes", 
        max_length=50, 
        default=""
    )
    
    fecha1 = models.TextField(
        verbose_name="Dia del mes. Ejemplo: Dia 02 - Dia Mundial de los humedales", 
        default="",
        blank=True,
        null=True
    )

    
    def __str__(self):
        return self.nombre
