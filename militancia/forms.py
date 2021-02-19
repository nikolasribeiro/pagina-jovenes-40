from django import forms
from .models import DatosObtenidos

class DatosObtenidosForm(forms.ModelForm):
    class Meta:
        model = DatosObtenidos
        fields = [
            'nombre',
            'email',
            'celular',
            'credencial',
            'departamento',
            'barrio',
            'municipio'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder':'Nombre Completo*', 'required':True}),
            'email': forms.EmailInput(attrs={'placeholder':'Email*', 'required':True}),
            'celular': forms.TextInput(attrs={'placeholder':'Celular*', 'required':True}),
            'credencial': forms.TextInput(attrs={'placeholder':'Credencial Civica'}),
            'departamento': forms.TextInput(attrs={'placeholder':'Departamento*', 'required':True}),
            'barrio': forms.TextInput(attrs={'placeholder':'Barrio*', 'required':True}),
            'municipio': forms.TextInput(attrs={'placeholder':'Municipio'}),
        }