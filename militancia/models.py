from django.db import models

# Create your models here.
class DatosObtenidos(models.Model):
    nombre          = models.CharField(default="", max_length=100)
    email           = models.EmailField(default="", max_length=100)
    celular         = models.CharField(default="", max_length=100)
    credencial      = models.CharField(default="", max_length=100, blank=True, null=True)
    departamento    = models.CharField(default="", max_length=100)
    barrio          = models.CharField(default="", max_length=100)
    municipio       = models.CharField(default="", max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nombre