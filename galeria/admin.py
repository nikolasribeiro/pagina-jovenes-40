from django.contrib import admin
from .models import Galeria


# Import Export para guardar datos
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Clases del import Export
class GaleriaResource(resources.ModelResource):
    class Meta:
        model = Galeria

class GaleriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'titulo_galeria',
        'imagen1',
        'imagen2',
        'imagen3',
        'imagen4',
        'imagen5',
        'imagen6',
        'imagen7',
        'imagen8',
        'imagen9',
        'imagen10',
    )

    resource_class = GaleriaResource


# Register your models here.
admin.site.register(Galeria, GaleriaAdmin)