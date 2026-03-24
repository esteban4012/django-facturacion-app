from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_factura),
    path("crear/", views.crear_factura),
]
