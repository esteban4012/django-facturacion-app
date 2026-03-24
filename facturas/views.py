from django.shortcuts import render,redirect
from .models import Factura
from .forms import FacturaForm

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
