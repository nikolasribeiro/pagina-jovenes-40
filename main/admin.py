from django.contrib import admin
from .models import *

# Import Export para guardar datos
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Clases del import Export
class NoticiasResource(resources.ModelResource):
    class Meta:
        model = Noticias

class FechasImportantesResource(resources.ModelResource):
    class Meta:
        model = FechasImportantes

class NoticiasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'titulo',
        'descripcion',
        'imagen',
        'autor',
        'fecha',
    )

    resource_class = NoticiasResource

class FechasImportantesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'nombre',
        'fecha1',
    )

    resource_class = FechasImportantesResource


# Register your models here.
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(FechasImportantes, FechasImportantesAdmin)