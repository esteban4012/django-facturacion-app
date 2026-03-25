from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from facturas.views import login_requerido_con_mensaje


@login_requerido_con_mensaje
def lista_producto(request):
    query = request.GET.get('q')

    productos = Producto.objects.all()

    if query:
        productos = productos.filter(
            nombre__icontains=query
        ) | productos.filter(
            id__icontains=query
        )

    return render(request, 'productos/lista.html', {
        'productos': productos
    })


@login_requerido_con_mensaje
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productos/')
    else:
        form = ProductoForm()
    return render(request,'productos/crear.html', {'form':form})


@login_requerido_con_mensaje
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


@login_requerido_con_mensaje
def eliminar_producto(request,id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/productos/')
