from django.shortcuts import render,redirect
from .models import Factura, DetalleFactura
from .forms import FacturaForm
from productos.models import Producto
from django.contrib import messages


def lista_factura(request):
    factura = Factura.objects.all()
    return render(request,'facturas/lista.html' ,{'factura': factura})

def crear_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/facturas/')
    else:
        form = FacturaForm()
    return render(request,'facturas/crear.html',{'form':form})

def detalle_factura(request, id):
    factura = Factura.objects.get(id=id)
    detalles = factura.detallefactura_set.all()
    productos = Producto.objects.all()

    return render(request, 'facturas/detalle.html', {
        'factura': factura,
        'detalles': detalles,
        'productos': productos
    })



def agregar_producto(request, id):
    if request.method == 'POST':
        factura = Factura.objects.get(id=id)
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad'))

        producto = Producto.objects.get(id=producto_id)

        # 🔥 VALIDACIÓN DE STOCK
        if producto.stock < cantidad:
            messages.error(request, "No hay suficiente stock")
            return redirect(f'/facturas/{id}/')

        # 🔥 DESCONTAR STOCK
        producto.stock -= cantidad
        producto.save()

        # 🔥 CREAR DETALLE
        DetalleFactura.objects.create(
            factura=factura,
            producto=producto,
            cantidad=cantidad
        )

        messages.success(request, "Producto agregado correctamente")

    return redirect(f'/facturas/{id}/')
