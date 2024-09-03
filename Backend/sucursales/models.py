from django.db import models

# Create your models here.

# Modelo de la tabla sucursal
class modelo_sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=100)
    direccion_sucursal = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre_sucursal}'

# Modelo de la tabla departamento
class modelo_departamento(models.Model):
    nombre_departamento = models.CharField(max_length=100)
    sucursal = models.ForeignKey(modelo_sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return f'departamento {self.nombre_departamento} de la sucursal {self.sucursal}'

# Modelo de la tabla proveedor
class modelo_proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=100)
    direccion_proveedor = models.CharField(max_length=100, blank=True, null=True)
    telefono_proveedor = models.CharField(max_length=100, blank=True, null=True)
    email_proveedor = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre_proveedor}'

# Modelo de la tabla producto
class modelo_producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    descripcion_producto = models.CharField(max_length=200, blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(modelo_proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre_producto}'

# Modelo de la tabla inventario
class modelo_inventario(models.Model):
    producto = models.ForeignKey(modelo_producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    sucursal = models.ForeignKey(modelo_sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.producto} en la sucursal {self.sucursal}'