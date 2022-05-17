from django import forms
from .models import Alumno

# creado metodo carretero
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('nombre', "apellido", "rut", "email", "pais", "ciudad")




"""
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    rut = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=True)
    pais = forms.CharField(max_length=30, required=True)
    ciudad = forms.CharField(max_length=30, required=True)
"""

"""
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    email = models.EmailField(verbose_name="Correo Alumno")
    pais = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
"""