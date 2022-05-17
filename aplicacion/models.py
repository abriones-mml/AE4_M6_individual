from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=10)
    email = models.EmailField(verbose_name="Correo Alumno")
    pais = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre
    
