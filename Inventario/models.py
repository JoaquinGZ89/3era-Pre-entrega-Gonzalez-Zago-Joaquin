from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    usuario = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    nombre_prod = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateField()

