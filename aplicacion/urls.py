from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("/alumnos", views.alumnos, name = "alumnos"),
    path("/ingreso", views.ingreso, name = "ingreso")
]