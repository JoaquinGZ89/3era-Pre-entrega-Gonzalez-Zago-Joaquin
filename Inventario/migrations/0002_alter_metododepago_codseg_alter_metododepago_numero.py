# Generated by Django 5.0.2 on 2024-03-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metododepago',
            name='codseg',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='metododepago',
            name='numero',
            field=models.CharField(max_length=16),
        ),
    ]
