from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def lista_producto(request):
    producto = Producto.objects.all()
    return render(request,'productos/lista.html', {'producto': producto})




