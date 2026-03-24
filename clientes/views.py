from django.shortcuts import render, redirect
from .models import Cliente

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes/lista.html", {"clientes":clientes})

