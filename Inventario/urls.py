from django.urls import path, include
from .views import *

urlpatterns = [ 
    path('', home, name="home"),
    path('tienda/', tienda, name="tienda"),
    path('tienda/graficas/', graficas, name="graficas"),
    path('tienda/procesadores/', procesadores, name="procesadores"),
    path('tienda/monitores/', monitores, name="monitores"),
    path('usuarios', usuarios_registrados, name = "usuarios"),
    path('registro/', registro, name="registro"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('producto', agregar_prod, name='producto'),
    path('buscar_prod', buscarProducto, name='buscarProducto'),
    path('encontrar_prod', encontrarProducto, name='encontrarProducto'),
    path('comprar', comprar, name='comprar'),
    path('tickets', tickets, name='tickets'),
]
