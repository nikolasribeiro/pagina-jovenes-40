from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField


# Create your models here.
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=255)
    slug_categoria   = AutoSlugField(populate_from='nombre_categoria', default='general', unique=True)

    class Meta:
        ordering = ('nombre_categoria',)
        verbose_name = 'Categoria'

    def __str__(self):
        return self.nombre_categoria



class Blog(models.Model):
    
    titulo_blog = models.CharField(
        verbose_name="Titulo del blog", 
        default="",
        max_length=35
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

    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    fecha_publicacion = models.DateTimeField(
        verbose_name="Fecha de Publicacion",
        auto_now_add=True,
        auto_now=False
    )

    def __str__(self):
        return self.titulo_blog


