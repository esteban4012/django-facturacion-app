from django.db import models
from clientes.models import Cliente

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return f"Factura {self.id} - {self.cliente.nombre}"
