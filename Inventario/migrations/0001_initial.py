# Generated by Django 5.0.2 on 2024-03-05 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoDePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('numero', models.IntegerField(max_length=16)),
                ('fecha_vencimiento', models.DateField()),
                ('codseg', models.IntegerField(max_length=4)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.cliente')),
                ('metodo_de_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.metododepago')),
                ('productos', models.ManyToManyField(to='Inventario.producto')),
            ],
        ),
    ]
