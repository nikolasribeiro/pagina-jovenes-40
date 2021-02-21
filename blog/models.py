from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField


# Create your models here.
class Blog(models.Model):
    
    titulo_blog = models.CharField(
        verbose_name="Titulo del blog", 
        default="",
        max_length=30
    )

    subtitulo_blog = models.CharField(
        verbose_name="Subtitulo del blog (Este campo puede estar vacio)",
        default="",
        max_length=50,
    )

    imagen_blog = models.URLField(
        verbose_name="URL de la Imagen",
        default="",
        max_length=600
    )

    slug = AutoSlugField(
        populate_from='titulo_blog'
    )

    descripcion_breve = models.TextField(
        verbose_name="Descripcion Breve",
        default=""
    )

    contenido_blog = RichTextField(
        verbose_name="Contenido del blog"
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    fecha_publicacion = models.DateTimeField(
        verbose_name="Fecha de Publicacion",
        auto_now_add=True,
        auto_now=False
    )

    def __str__(self):
        return self.titulo_blog