from django.db import models

# Create your models here.
class Galeria(models.Model):
    
    titulo_galeria  = models.CharField(
        verbose_name="Titulo de la galeria", 
        default="", 
        max_length=200
    )

    imagen1         = models.URLField(
        verbose_name="URL de la Imagen",
        default="",
        max_length=600
    )

    imagen2         = models.URLField(
        verbose_name="URL de la Imagen",
        default="",
        max_length=600
    )

    imagen3         = models.URLField(
        verbose_name="URL de la Imagen",
        default="",
        max_length=600
    )

    imagen4         = models.URLField(
        verbose_name="URL de la Imagen",
        default="",
        max_length=600
    )

    imagen5         = models.URLField(
        verbose_name="URL de la Imagen",
        default="",
        max_length=600
    )

    imagen6         = models.URLField(
        verbose_name="URL de la Imagen",
        default="",
        max_length=600
    )

    imagen7         = models.URLField(
        verbose_name="URL de la Imagen",
        default="",
        max_length=600
    )

    imagen8         = models.URLField(
        verbose_name="URL de la Imagen",
        default="",
        max_length=600
    )

    imagen9         = models.URLField(
        verbose_name="URL de la Imagen",
        default="",
        max_length=600
    )

    imagen10        = models.URLField(
        verbose_name="URL de la Imagen",
        default="",
        max_length=600
    )

    def __str__(self):
        return self.titulo_galeria
