# Generated by Django 5.1 on 2024-09-01 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sucursales", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="modelo_producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_producto", models.CharField(max_length=100)),
                ("descripcion_producto", models.CharField(max_length=200)),
                ("sku", models.CharField(max_length=100, unique=True)),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="modelo_proveedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_proveedor", models.CharField(max_length=100)),
                ("direccion_proveedor", models.CharField(max_length=100)),
                ("telefono_proveedor", models.CharField(max_length=100)),
                ("email_proveedor", models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="modelo_inventario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad", models.IntegerField()),
                (
                    "sucursal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sucursales.modelo_sucursal",
                    ),
                ),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sucursales.modelo_producto",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="modelo_producto",
            name="proveedor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="sucursales.modelo_proveedor",
            ),
        ),
    ]
