from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from facturas.models import Factura
from clientes.models import Cliente
from productos.models import Producto
from django.db.models import Sum
from datetime import date

@login_required
def dashboard(request):
    total_facturado = Factura.objects.aggregate(Sum('total'))['total__sum'] or 0
    total_facturas = Factura.objects.count()
    total_clientes = Cliente.objects.count()

    hoy = date.today()
    ventas_hoy = Factura.objects.filter(fecha=hoy).aggregate(Sum('total'))['total__sum'] or 0

    productos_bajo_stock = Producto.objects.filter(stock__lt=5)

    context = {
        'total_facturado': total_facturado,
        'total_facturas': total_facturas,
        'total_clientes': total_clientes,
        'ventas_hoy': ventas_hoy,
        'productos_bajo_stock': productos_bajo_stock
    }

    return render(request, 'dashboard.html', context)

def home(request):
    return render(request,'home.html')

