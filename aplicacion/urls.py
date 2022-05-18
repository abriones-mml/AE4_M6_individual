from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = "index"),
    path("listado-alumno/", views.alumnos, name = "listado"),
    path("registro-alumno/", views.registro_alumno, name = "registro-alumno")
]