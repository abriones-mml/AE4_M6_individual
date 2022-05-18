from django.shortcuts import render
from .models import Alumno
from .forms import AlumnoForm

# Create your views here.
def index(request):
    return render(request, "aplicacion/index.html")

def alumnos(request):
    datos_alumnos = Alumno.objects.all() #.values?
    return render(request, "aplicacion/alumnos/listado.html", {'context': datos_alumnos})

def registro_alumno(request):
    form = AlumnoForm()
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = Alumno()
            alumno.nombre = form.cleaned_data["nombre"]
            alumno.apellido = form.cleaned_data["apellido"]
            alumno.rut = form.cleaned_data["rut"]
            alumno.email = form.cleaned_data["email"]
            alumno.ciudad = form.cleaned_data["ciudad"]
            alumno.pais = form.cleaned_data["pais"]
            alumno.save()
    return render(request, "aplicacion/alumnos/registro.html", {"form": form})