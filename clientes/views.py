from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
from facturas.views import login_requerido_con_mensaje


@login_requerido_con_mensaje
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes/lista.html", {"clientes":clientes})


@login_requerido_con_mensaje
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientes/')
    else:
        form = ClienteForm()
    return render(request,'clientes/crear.html',{'form':form})
        

@login_requerido_con_mensaje
def editar_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('/clientes/')
    else:
        form = ClienteForm(instance=cliente)
    return render(request,'clientes/editar.html',{'form':form})


@login_requerido_con_mensaje
def eliminar_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/clientes/')