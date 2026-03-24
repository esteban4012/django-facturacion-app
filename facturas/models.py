from django.db import models
from clientes.models import Cliente
from productos.models import Producto

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return f"Factura {self.id} - {self.cliente.nombre}"


class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10,decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"
    
    def save(self, *args, **kwargs):
        self.subtotal = self.producto.precio * self.cantidad
        super().save(*args, **kwargs)

        # actualizar total de factura
        total = sum(det.subtotal for det in self.factura.detallefactura_set.all())
        self.factura.total = total
        self.factura.save()