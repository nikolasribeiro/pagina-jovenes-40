from django.contrib import admin
from .models import Blog, Categoria



# Import Export para guardar datos
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Clases del import Export
class BlogResource(resources.ModelResource):
    class Meta:
        model = Blog

class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'titulo_blog',
        'subtitulo_blog',
        'imagen_blog',
        'slug',
        'descripcion_breve',
        'contenido_blog',
        'autor',
        'fecha_publicacion',
    )

    resource_class = BlogResource


class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Blog

class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'nombre_categoria',
    )

    resource_class = CategoriaResource



# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Categoria, CategoriaAdmin)