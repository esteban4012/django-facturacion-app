from django.shortcuts import get_object_or_404, render,redirect
from .models import Factura, DetalleFactura
from .forms import FacturaForm
from productos.models import Producto
from django.contrib import messages
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def lista_factura(request):
    facturas = Factura.objects.all()
    return render(request,'facturas/lista.html' ,{'facturas': facturas})

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

        # VALIDACIÓN DE STOCK
        if producto.stock < cantidad:
            messages.error(request, "No hay suficiente stock")
            return redirect(f'/facturas/{id}/')

        # DESCONTAR STOCK
        producto.stock -= cantidad
        producto.save()

        # CREAR DETALLE
        DetalleFactura.objects.create(
            factura=factura,
            producto=producto,
            cantidad=cantidad
        )

        messages.success(request, "Producto agregado correctamente")

    return redirect(f'/facturas/{id}/')



def factura_pdf(request, id):
    factura = Factura.objects.get(id=id)
    detalles = factura.detallefactura_set.all()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{id}.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    contenido = []

    contenido.append(Paragraph(f"Factura #{factura.id}", styles['Title']))
    contenido.append(Paragraph(f"Cliente: {factura.cliente.nombre}", styles['Normal']))
    contenido.append(Paragraph(f"Fecha: {factura.fecha}", styles['Normal']))

    for d in detalles:
        contenido.append(Paragraph(
            f"{d.producto.nombre} - {d.cantidad} x {d.producto.precio} = {d.subtotal}",
            styles['Normal']
        ))

    contenido.append(Paragraph(f"Total: {factura.total}", styles['Title']))

    doc.build(contenido)

    return response


def eliminar_factura(request, id):
    factura = get_object_or_404(Factura, id=id)
    factura.delete()
    return redirect('lista_facturas')

def eliminar_detalle(request, id):
    detalle = get_object_or_404(DetalleFactura, id=id)
    producto = detalle.producto
    factura = detalle.factura
    producto.stock += detalle.cantidad
    producto.save()
    detalle.delete()
    total = 0
    detalles = factura.detallefactura_set.all()

    for d in detalles:
        total += d.subtotal
    factura.total = total
    factura.save()
    return redirect('detalle_factura', id=factura.id)