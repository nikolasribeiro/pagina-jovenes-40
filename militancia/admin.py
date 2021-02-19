from django.contrib import admin
from .models import DatosObtenidos


# Import Export para guardar datos
from import_export import resources
from import_export.admin import ImportExportModelAdmin


# Clases del import Export
class DatosObtenidosResource(resources.ModelResource):
    class Meta:
        model = DatosObtenidos

class DatosObtenidosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'nombre',
        'email',
        'celular',
        'credencial',
        'departamento',
        'barrio',
        'municipio',
    )

    resource_class = DatosObtenidosResource


# Register your models here.
admin.site.register(DatosObtenidos, DatosObtenidosAdmin)