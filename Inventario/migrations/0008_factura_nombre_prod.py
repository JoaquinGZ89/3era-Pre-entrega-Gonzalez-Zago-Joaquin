# Generated by Django 5.0.2 on 2024-03-12 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0007_factura_remove_detallecarrito_carrito_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='nombre_prod',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
