from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_factura, name='lista_facturas'),
    path("crear/", views.crear_factura),
    path('<int:id>/', views.detalle_factura, name='detalle_factura'),
    path('<int:id>/agregar/', views.agregar_producto),
    path('<int:id>/pdf/', views.factura_pdf),
    path('eliminar/<int:id>/', views.eliminar_factura, name='eliminar_factura'),
    path('detalle/eliminar/<int:id>/', views.eliminar_detalle, name='eliminar_detalle'),
]
