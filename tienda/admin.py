from django.contrib import admin
from .models import Empleado, Proveedor, Producto, Venta, DetalleVenta

admin.site.register(Empleado)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
