# Generated by Django 5.1 on 2024-09-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "sucursales",
            "0002_modelo_producto_modelo_proveedor_modelo_inventario_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelo_producto",
            name="descripcion_producto",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="modelo_proveedor",
            name="direccion_proveedor",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="modelo_proveedor",
            name="email_proveedor",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="modelo_proveedor",
            name="telefono_proveedor",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="modelo_sucursal",
            name="direccion_sucursal",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
