from django.contrib import admin

# Ingresar los modelos aquí
from .models import modelo_sucursal, modelo_departamento, modelo_proveedor, modelo_producto, modelo_inventario

# Clase para los modelos de administracion
class vista_admin_inventario(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'sucursal')
    search_fields = ('sucursal__nombre_sucursal', 'producto__nombre_producto')
    list_filter = ("sucursal__nombre_sucursal",)

class vista_admin_producto(admin.ModelAdmin):
    list_display = ("sku", "nombre_producto", "precio", "proveedor")
    search_fields = ("sku", "nombre_producto", "proveedor__nombre_proveedor")

class vista_admin_proveedor(admin.ModelAdmin):
    list_display = ("nombre_proveedor", "telefono_proveedor", "email_proveedor")
    search_fields = ("nombre_proveedor", "telefono_proveedor", "email_proveedor")

# Paginas de administración aqui
admin.site.register(modelo_sucursal)
admin.site.register(modelo_departamento)
admin.site.register(modelo_proveedor, vista_admin_proveedor)
admin.site.register(modelo_producto, vista_admin_producto)
admin.site.register(modelo_inventario, vista_admin_inventario)
