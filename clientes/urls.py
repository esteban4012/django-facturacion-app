from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_clientes),
    path("crear/", views.crear_cliente),
    path("editar/<int:id>/", views.editar_cliente),
]
