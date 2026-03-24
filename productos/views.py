from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def lista_producto(request):
    producto = Producto.objects.all()
    return render(request,'productos/lista.html', {'producto': producto})



def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productos/')
    else:
        form = ProductoForm()
    return render(request,'productos/crear.html', {'form':form})

def editar_producto(request,id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('/productos/')
    else:
        form = ProductoForm(instance=producto)
    return render(request,'productos/editar.html',{'form':form})



