from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_producto),
    path("crear/", views.crear_producto),
    path("editar/<int:id>/", views.editar_producto)
]
